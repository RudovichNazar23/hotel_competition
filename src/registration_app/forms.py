from django import forms
from .models import HighSchool, Guardian, TeamMember


class CreateHighSchoolForm(forms.ModelForm):
    class Meta:
        model = HighSchool
        fields = "__all__"


class CreateGuardianForm(forms.ModelForm):
    class Meta:
        model = Guardian
        fields = "__all__"


class CreateTeamMemberForm(forms.ModelForm):
    class Meta:
        model = TeamMember
        fields = "__all__"


