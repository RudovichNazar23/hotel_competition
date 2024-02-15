from django import forms

from .models import OpenRegistration


class OpenRegistrationForm(forms.ModelForm):
    class Meta:
        model = OpenRegistration
        fields = "__all__"

        widgets = {
            "date_from": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "date_to": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
        }
