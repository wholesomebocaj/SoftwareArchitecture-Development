from django import forms
from django.core.exceptions import ValidationError
from .models import Complaint
import re


class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ["title", "description", "category"]

        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control",
                "maxlength": "100"
            }),
            "description": forms.Textarea(attrs={
                "rows": 4,
                "class": "form-control",
                "maxlength": "1000"
            }),
            "category": forms.TextInput(attrs={
                "class": "form-control",
                "maxlength": "50"
            }),
        }

    # SECURITY FIX
    # Fix ID: F3 – Server-side complaint form validation
    # Weakness ID: W3
    # STRIDE: Tampering
    # OWASP Top 10: A03 Injection
    # CWE: CWE-20 Improper Input Validation
    # CIA: Integrity
    # ASVS: V5 Input Validation
    # D3FEND: D3-DLV Domain Logic Validation
    def clean_title(self):
        title = self.cleaned_data.get("title", "").strip()

        if len(title) < 5:
            raise ValidationError("Title must be at least 5 characters long.")

        if len(title) > 100:
            raise ValidationError("Title must be no more than 100 characters long.")

        if re.search(r"[<>;$]", title):
            raise ValidationError("Title contains invalid characters.")

        return title

    def clean_description(self):
        description = self.cleaned_data.get("description", "").strip()

        if len(description) < 20:
            raise ValidationError("Description must be at least 20 characters long.")

        if len(description) > 1000:
            raise ValidationError("Description must be no more than 1000 characters long.")

        suspicious_patterns = [
            r"<script",
            r"javascript:",
            r"DROP\s+TABLE",
            r"UNION\s+SELECT",
            r"--",
        ]

        for pattern in suspicious_patterns:
            if re.search(pattern, description, re.IGNORECASE):
                raise ValidationError("Description contains suspicious input.")

        return description

    def clean_category(self):
        category = self.cleaned_data.get("category", "").strip()

        allowed_categories = [
            "Billing",
            "Account",
            "Technical",
            "Refund",
            "Card",
            "Broadband",
            "Other",
        ]

        if category not in allowed_categories:
            raise ValidationError("Please select a valid complaint category.")

        return category