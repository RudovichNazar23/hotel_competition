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
        high_school_form = CreateHighSchoolForm(request.POST)
        guardian_form = CreateGuardianForm(request.POST, request.FILES)
        first_team_member_form = CreateTeamMemberForm(request.POST, request.FILES)

        second_member_data = self.get_form_data(form_fields=["second_member_name", "second_member_surname"])

        if high_school_form.is_valid() and guardian_form.is_valid() and first_team_member_form.is_valid():
            high_school_object = high_school_form.save()
            guardian_object = guardian_form.save()
            first_member_object = first_team_member_form.save()
            second_member_object = None

            if second_member_data:
                second_member_form = CreateTeamMemberForm(second_member_data, request.FILES)
                if second_member_form.is_valid():
                    second_member_object = create_model_object(model=self.team_member_form.model,
                                                               member_name=second_member_data.get("second_member_name"),
                                                               member_surname=second_member_data.get(
                                                                   "second_member_surname"),
                                                               member_clause=request.FILES.get("second_member_clause"))
            school_team_object = create_model_object(model=SchoolTeam, high_school=high_school_object,
                                                     guardian=guardian_object, first_member=first_member_object,
                                                     second_member=second_member_object)
            # self.send_email_to_client(
            #     (
            #         self.create_message(high_school_data.get("school_email")),
            #         self.create_message(guardian_form_data.get("guardian_email"))
            #     )
            # )
            return JsonResponse(
                data={"status": 200, "message": "Your team is created", "success_url_name": "success_page"},
                status=200
                )
        else:
            return JsonResponse(data={"status": 400, "message": "Form is not valid", "error_url_name": "error_page"}, status=200)


class SuccessPageView(TemplateView):
    template_name = "registration_app/success_page.html"
