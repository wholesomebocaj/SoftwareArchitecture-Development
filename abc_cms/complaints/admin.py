from django.contrib import admin
from .models import Complaint, ComplaintStatusHistory

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "company",
        "created_by",
        "status",
        "priority",
        "created_at",
    )
    list_filter = ("company", "status", "priority")
    search_fields = ("title", "description")

@admin.register(ComplaintStatusHistory)
class ComplaintStatusHistoryAdmin(admin.ModelAdmin):
    list_display = ("complaint", "old_status", "new_status", "changed_by", "changed_at")
    list_filter = ("old_status", "new_status")
