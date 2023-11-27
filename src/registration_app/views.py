from django.shortcuts import render, redirect
from django.views.generic.base import View, TemplateView
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from .forms import CreateHighSchoolForm, CreateGuardianForm, CreateTeamMemberForm
from .models import SchoolTeam

from service.mixins.get_model_by_form_field import GetModelByFormFieldMixin
from service.mixins.get_form_data_mixin import GetFormDataMixin
from service.mixins.create_model_object_mixin import CreateModelObjectMixin

from service.create_model_object import create_model_object
from service.send_email_to_client import SendMailToClientMixin


class RegistrationView(View, GetModelByFormFieldMixin):
    template_name = "registration_app/registration_form.html"
    high_school_form = CreateHighSchoolForm()
    guardian_form = CreateGuardianForm()
    team_member_form = CreateTeamMemberForm()

    def get(self, request):
        return render(request, template_name=self.template_name, context={
            "high_school_form": self.high_school_form,
            "guardian_form": self.guardian_form,
            "team_member_form": self.team_member_form,
        })

    def post(self, request):
        field_name = str(request.POST.get("field_name"))
        field_value = str(request.POST.get("field_value"))
        model = self.get_model_by_field(form_classes=[self.high_school_form, self.guardian_form, self.guardian_form],
                                        field=field_name
                                        )
        try:
            get_object_or_404(klass=model, **{field_name: field_value})
            return JsonResponse(
                data={
                    "status": 400,
                    "message": "Object with this data already exists"
                },
                status=200
            )
        except Exception as exception:
            return JsonResponse(
                data={
                    "status": 200,
                },
                status=200
            )


class CreateSchoolTeamView(View, GetFormDataMixin, CreateModelObjectMixin, SendMailToClientMixin):
    high_school_form = CreateHighSchoolForm()
    guardian_form = CreateGuardianForm()
    team_member_form = CreateTeamMemberForm()
    subject = "Test email"
    message_body = "Your school has been successfully registered"

    def post(self, request):
        high_school_data = self.get_form_data(
            form_fields=self.high_school_form.fields.keys(),
        )
        guardian_form_data = self.get_form_data(
            form_fields=self.guardian_form.fields.keys(),
            # keys_to_delete=["guardian_clause"]
        )
        first_team_member_form_data = self.get_form_data(
            form_fields=self.team_member_form.fields.keys(),
            # keys_to_delete=["member_clause"]
        )
        high_school_object = self.create_object(self.high_school_form.model, high_school_data)
        guardian_object = self.create_object(self.guardian_form.model, guardian_form_data)
        first_team_member_object = self.create_object(self.team_member_form.model, first_team_member_form_data,
                                                      )

        school_team = create_model_object(model=SchoolTeam, high_school=high_school_object, guardian=guardian_object)
        school_team.members.add(first_team_member_object)

        second_team_member_form_data = {"member_name": request.POST.get("second_member_name"),
                                        "member_surname": request.POST.get("second_member_surname")}
        if self.check_form_data(second_team_member_form_data):
            second_team_member = create_model_object(self.team_member_form.model,
                                                     member_clause=self.request.FILES.get("second_member_clause"),
                                                     **second_team_member_form_data)
            school_team.members.add(second_team_member)

        self.send_email_to_client(
            (
                self.create_message(high_school_data.get("school_email")),
                self.create_message(guardian_form_data.get("guardian_email"))
            )
        )
        return JsonResponse(
            data={
                "status": 200,
                "message": "Your team is created",
                "success_url_name": "success_page"
            },
            status=200
        )


class SuccessPageView(TemplateView):
    template_name = "registration_app/success_page.html"
