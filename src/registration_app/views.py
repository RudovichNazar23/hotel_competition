from django.shortcuts import render
from django.views.generic.base import View

from .forms import CreateHighSchoolForm, CreateGuardianForm, CreateTeamMemberForm


class RegistrationView(View):
    template_name = "registration_app/registration_form.html"
    high_school_form = CreateHighSchoolForm()
    guardian_form = CreateGuardianForm()
    team_member_form = CreateTeamMemberForm()

    def get(self, request):
        return render(request, template_name=self.template_name, context={
            "high_school_form": self.high_school_form,
            "guardian_form": self.guardian_form,
            "team_form": self.team_member_form
        })


