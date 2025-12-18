from django.db import models
from django.conf import settings

# Create your models here.

# multi-tenancy by assigning users and complaints to a company
class Company(models.Model):
    INDUSTYRY_CHOICES = [
        ("BANK", "Banking"),    
        ("TELECOM", "Telecom"),
        ("AIRLINE", "Airline"),
    ]

    name = models.CharField(max_length=255)
    industry = models.CharField(max_length=20, choices=INDUSTYRY_CHOICES)

    class Meta:
            verbose_name = "Company"
            verbose_name_plural = "Companies"  # fixes plural in admin


    # makes the object readable in Django admin
    def __str__(self):
        return self.name
    
class UserProfile(models.Model):
    ROLE_CHOICES = [
        ("CONSUMER", "Consumer"),
        ("AGENT", "Helpdesk Agent"),
        ("SUPPORT", "Support Egnineer"),
        ("MANAGER", "Helpdesk Manager"),
        ("ADMIN", "System Administrator"),
    ]

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile")
    
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="profile")
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    class Meta:
        verbose_name = "User profile"
        verbose_name_plural = "User profiles"  

    def __str__(self):
        return f"{self.user.username} ({self.role} @ {self.company.name})"