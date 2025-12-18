from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render
from .forms import ComplaintForm
from .models import Complaint, ComplaintStatusHistory
from django.core.paginator import Paginator

@login_required
def complaint_home(request):
    # redirects to the users complaint list.
    return redirect("complaint_list")


@login_required
def create_complaint(request):
    # only allow consumers to use this view
    if request.user.profile.role != "CONSUMER":
        raise PermissionDenied("Only consumers can submit complaints.")

    if request.method == "POST":
        form = ComplaintForm(request.POST)
        if form.is_valid():
            complaint = form.save(commit=False)

            # fields that must be set server-side
            complaint.company = request.user.profile.company
            complaint.created_by = request.user
            complaint.channel = "WEB"  

            complaint.save()
            return redirect("complaint_list")
    else:
        form = ComplaintForm()

    return render(
        request,
        "complaints/complaint_form.html", 
        {"form": form},
    )


@login_required
def complaint_list(request):
    profile = getattr(request.user, "profile", None)
    if not profile or profile.role != "CONSUMER":
        raise PermissionDenied("Only consumers can view their complaints.")

    complaints_qs = Complaint.objects.filter(
        created_by=request.user,
        company=profile.company,
    )

    # filters 
    status_filter = request.GET.get("status") or ""       
    priority_filter = request.GET.get("priority") or ""   

    allowed_statuses = [code for code, _ in Complaint.STATUS_CHOICES]
    allowed_priorities = [code for code, _ in Complaint.PRIORITY_CHOICES]

    if status_filter and status_filter in allowed_statuses:
        complaints_qs = complaints_qs.filter(status=status_filter)

    if priority_filter and priority_filter in allowed_priorities:
        complaints_qs = complaints_qs.filter(priority=priority_filter)

    # sorting 
    allowed_sorts = {
        "id": "id",
        "title": "title",
        "category": "category",
        "status": "status",
        "priority": "priority",
        "created": "created_at",
    }

    sort = request.GET.get("sort", "created")
    direction = request.GET.get("direction", "desc")

    sort_field = allowed_sorts.get(sort, "created_at")
    order_by = sort_field if direction == "asc" else f"-{sort_field}"

    complaints_qs = complaints_qs.order_by(order_by)

    # pagination 
    paginator = Paginator(complaints_qs, 10)  
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "complaints/complaint_list.html",
        {
            "complaints": page_obj,
            "page_obj": page_obj,
            "current_sort": sort,
            "current_direction": direction,
            "status_choices": Complaint.STATUS_CHOICES,
            "priority_choices": Complaint.PRIORITY_CHOICES,
            "current_status": status_filter,
            "current_priority": priority_filter,
        },
    )

@login_required
def complaint_detail(request, pk):
    complaint = get_object_or_404(
        Complaint,
        pk=pk,
        created_by=request.user,
        company=request.user.profile.company,
    )

    return render(
        request,
        'complaints/complaint_detail.html',
        {'complaint': complaint}
    )

@login_required
def agent_complaint_list(request):
    profile = getattr(request.user, 'profile', None)

    if not profile or profile.role not in ("AGENT", "SUPPORT", "MANAGER"):
        raise PermissionDenied("You do not have access to the agent view.")
    
    complaints_qs = Complaint.objects.filter(
        company=profile.company
    )

    # filters 
    status_filter = request.GET.get("status") or ""       
    priority_filter = request.GET.get("priority") or ""   

    allowed_statuses = [code for code, _ in Complaint.STATUS_CHOICES]
    allowed_priorities = [code for code, _ in Complaint.PRIORITY_CHOICES]

    if status_filter and status_filter in allowed_statuses:
        complaints_qs = complaints_qs.filter(status=status_filter)

    if priority_filter and priority_filter in allowed_priorities:
        complaints_qs = complaints_qs.filter(priority=priority_filter)

    # sorting
    allowed_sorts = {
        "id": "id",
        "title": "title",
        "category": "category",
        "status": "status",
        "priority": "priority",
        "created": "created_at",
    }

    sort = request.GET.get("sort", "created")
    direction = request.GET.get("direction", "desc")

    sort_field = allowed_sorts.get(sort, "created_at")
    order_by = sort_field if direction == "asc" else f"-{sort_field}"
    complaints_qs = complaints_qs.order_by(order_by)

    # pagination
    paginator = Paginator(complaints_qs, 20)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "complaints/agent_complaint_list.html",
        {
            "complaints": page_obj,
            "page_obj": page_obj,
            "current_sort": sort,
            "current_direction": direction,
            "status_choices": Complaint.STATUS_CHOICES,
            "priority_choices": Complaint.PRIORITY_CHOICES,
            "current_status": status_filter,
            "current_priority": priority_filter,
        },
    )



@login_required
def agent_complaint_detail(request, pk):
    profile = getattr(request.user, 'profile', None)

    if not profile or profile.role not in ("AGENT", "SUPPORT", "MANAGER"):
        raise PermissionDenied("You do not have access to the agent view.")

    complaint = get_object_or_404(
        Complaint,
        pk=pk,
        company=profile.company,
    )

    if request.method == "POST":
        old_status = complaint.status
        old_priority = complaint.priority

        new_status = request.POST.get("status", complaint.status)
        new_priority = request.POST.get("priority", complaint.priority)

        valid_statuses = dict(Complaint.STATUS_CHOICES).keys()
        valid_priorities = dict(Complaint.PRIORITY_CHOICES).keys()

        if new_status in valid_statuses:
            complaint.status = new_status
        if new_priority in valid_priorities:
            complaint.priority = new_priority

        complaint.save()

        status_changed = old_status != complaint.status
        priority_changed = old_priority != complaint.priority

        if status_changed or priority_changed:
            note_parts = []
            if status_changed:
                note_parts.append(f"Status: {old_status} → {complaint.status}")
            if priority_changed:
                note_parts.append(f"Priority: {old_priority} → {complaint.priority}")

            ComplaintStatusHistory.objects.create(
                complaint=complaint,
                old_status=old_status,
                new_status=complaint.status,
                changed_by=request.user,
                note="; ".join(note_parts),
            )

        return redirect("agent_complaint_detail", pk=complaint.pk)

    return render(
        request,
        "complaints/agent_complaint_detail.html",
        {
            "complaint": complaint,
            "status_choices": Complaint.STATUS_CHOICES,
            "priority_choices": Complaint.PRIORITY_CHOICES,
            "history": complaint.history.all(),
        },
    )
