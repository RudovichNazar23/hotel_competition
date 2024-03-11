from django import forms
from registration_app.models import TeamMember


class TestLoginForm(forms.ModelForm):
    class Meta:
        model = TeamMember
        fields = ("member_name", "member_surname")

        widgets = {
            "member_name": forms.TextInput(attrs={"class": "form-control"}),
            "member_surname": forms.TextInput(attrs={"class": "form-control"}),
        }

