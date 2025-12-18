from django import forms
from .models import Complaint


class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint

        # only fields the user should enter manually
        fields = ["title", "description", "category"]

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(
                attrs={"rows": 4, "class": "form-control"}
            ),
            "category": forms.TextInput(attrs={"class": "form-control"}),
        }

    