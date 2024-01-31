from django import forms

from .models import OpenRegistration


class OpenRegistrationForm(forms.ModelForm):
    class Meta:
        model = OpenRegistration
        fields = "__all__"

        widgets = {
            "date": forms.SelectDateWidget(attrs={"type": "date", "class": "form-control"}),
            "time_from": forms.TimeInput(attrs={"type": "time", "class": "form-control"},),
            "time_to": forms.TimeInput(attrs={"type": "time", "class": "form-control"})
        }
