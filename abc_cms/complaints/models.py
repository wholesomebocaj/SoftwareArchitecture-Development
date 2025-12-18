from django.conf import settings
from django.db import models
from accounts.models import Company

class Complaint(models.Model):
    STATUS_CHOICES = (
        ("OPEN", "Open"),
        ("IN_PROGRESS", "In Progress"),
        ("PENDING_CUSTOMER", "Pending Customer"),
        ("RESOLVED", "Resolved"),
        ("CLOSED", "Closed"),
    )

    PRIORITY_UNASSIGNED = "UNASSIGNED"
    PRIORITY_LOW = "LOW"
    PRIORITY_MEDIUM = "MEDIUM"
    PRIORITY_HIGH = "HIGH"

    PRIORITY_CHOICES = [
        (PRIORITY_UNASSIGNED, "Unassigned"),
        (PRIORITY_LOW, "Low"),
        (PRIORITY_MEDIUM, "Medium"),
        (PRIORITY_HIGH, "High"),
    ]

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="complaints_created",
    )
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="complaints_assigned",
        null=True,
        blank=True,
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=100)


    priority = models.CharField(
        max_length=20,             
        choices=PRIORITY_CHOICES,
        default=PRIORITY_UNASSIGNED,
    )

    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="OPEN"
    )

    channel = models.CharField(
        max_length=20,
        default="WEB",
        choices=(("WEB", "Web"), ("PHONE", "Phone")),
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"#{self.id} {self.title} [{self.get_status_display()}]"



class ComplaintStatusHistory(models.Model):
    complaint = models.ForeignKey(
        Complaint, on_delete=models.CASCADE, related_name="history"
    )
    old_status = models.CharField(max_length=20)
    new_status = models.CharField(max_length=20)
    changed_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    note = models.TextField(blank=True)
    changed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["changed_at"]
        verbose_name = "Complaint status history"
        verbose_name_plural = "Complaint status histories" 


    def __str__(self):
        return f"{self.complaint_id}: {self.old_status} → {self.new_status}"
