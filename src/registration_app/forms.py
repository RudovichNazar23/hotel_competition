from django import forms
from .models import HighSchool, Guardian, TeamMember

from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox


class BaseCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._add_form_control_attr()

    def _add_form_control_attr(self):
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})


class CreateHighSchoolForm(BaseCreateForm):
    model = HighSchool

    class Meta:
        model = HighSchool
        fields = "__all__"


class CreateGuardianForm(BaseCreateForm):
    model = Guardian

    class Meta:
        model = Guardian
        fields = "__all__"


class CreateTeamMemberForm(BaseCreateForm):
    model = TeamMember

    class Meta:
        model = TeamMember
        fields = "__all__"


class RecaptchaForm(forms.Form):
    recaptcha = ReCaptchaField()
