from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse


# after a successful login, decide where to send the user based on their role / privileges.
@login_required
def post_login_redirect(request):
    user = request.user
    if user.is_superuser:
        return redirect(reverse('admin:index'))

    profile = getattr(user, 'profile', None)

    if profile:
        if profile.role == 'CONSUMER':
            return redirect('complaint_list')
        
        if profile.role in ('AGENT', 'SUPPORT', 'MANAGER'):
            return redirect('agent_complaint_list')
        
    return redirect("complaint_list")

# return the correct dashboard URL for the given user.
def get_dashboard_url(user):
    if user.is_superuser:
        return "/admin/"

    profile = getattr(user, "profile", None)
    if not profile:
        return "/complaints/list/"  
    
    if profile.role == "CONSUMER":
        return "/complaints/list/"
    
    if profile.role in ("AGENT", "SUPPORT", "MANAGER", "ADMIN"):
        return "/complaints/agent/"

    return "/complaints/list/"  
