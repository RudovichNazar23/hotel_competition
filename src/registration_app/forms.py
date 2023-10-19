from django import forms
from .models import HighSchool, Guardian, TeamMember


class BaseCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._add_form_control_attr()

    def _add_form_control_attr(self):
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})


class CreateHighSchoolForm(BaseCreateForm):
    class Meta:
        model = HighSchool
        fields = "__all__"


class CreateGuardianForm(BaseCreateForm):
    class Meta:
        model = Guardian
        fields = "__all__"


class CreateTeamMemberForm(BaseCreateForm):
    class Meta:
        model = TeamMember
        fields = "__all__"


