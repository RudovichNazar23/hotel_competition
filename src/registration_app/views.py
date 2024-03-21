from django.shortcuts import render, redirect
from django.views.generic.base import View, TemplateView
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str

from .forms import CreateHighSchoolForm, CreateGuardianForm, CreateTeamMemberForm, RecaptchaForm
from .models import SchoolTeam
from django.contrib.auth.models import User

from service.mixins.get_model_by_form_field import GetModelByFormFieldMixin
from service.mixins.get_form_data_or_none_mixin import GetFormDataOrNoneMixin
from service.mixins.create_model_object_mixin import CreateModelObjectMixin
from service.mixins.create_object_or_get_none import CreateObjectOrGetNoneMixin
from service.mixins.check_opened_registration import CheckOpenedRegistrationMixin

from service.create_model_object import create_model_object
from service.get_closest_test import get_closest_test_by_opening_date
from service.send_email_to_client import SendMailToClientMixin
from service.tokens import account_activation_token


class RegistrationView(CheckOpenedRegistrationMixin, View, GetModelByFormFieldMixin):
    template_name = "registration_app/registration_form.html"
    high_school_form = CreateHighSchoolForm()
    guardian_form = CreateGuardianForm()
    team_member_form = CreateTeamMemberForm()
    recaptcha_form = RecaptchaForm()

    error_template_name = "admin_app/registration_is_not_activated.html"

    def get(self, request):
        return render(request, template_name=self.template_name, context={
            "high_school_form": self.high_school_form,
            "guardian_form": self.guardian_form,
            "team_member_form": self.team_member_form,
            "recaptcha_form": self.recaptcha_form
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
                    "message": "Takie dane już istnieją"
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


class CreateSchoolTeamView(View, GetFormDataOrNoneMixin, CreateModelObjectMixin, SendMailToClientMixin,
                           CreateObjectOrGetNoneMixin):
    high_school_form = CreateHighSchoolForm()
    guardian_form = CreateGuardianForm()
    team_member_form = CreateTeamMemberForm()
    mail_subject = "Link do potwierdzenia rejestracji"
    email_template_name = "registration_app/email_activation.html"

    def post(self, request):
        high_school_form = CreateHighSchoolForm(request.POST)
        guardian_form = CreateGuardianForm(request.POST, request.FILES)
        first_team_member_form = CreateTeamMemberForm(request.POST, request.FILES)

        second_member_data = self.get_form_data_or_none(request_keys=["second_member_name", "second_member_surname"],
                                                        form_keys=self.team_member_form.__dict__["fields"].keys())
        recaptcha = RecaptchaForm(request.POST)

        if high_school_form.is_valid() and guardian_form.is_valid() and first_team_member_form.is_valid() and recaptcha.is_valid():
            high_school_object = high_school_form.save()
            guardian_object = guardian_form.save()
            first_member_object = first_team_member_form.save()
            second_member_object = self.create_object_or_get_none(form_data=second_member_data,
                                                                  form_class=CreateTeamMemberForm, files_upload=True,
                                                                  file_key="second_member_clause",
                                                                  form_file_field_key="member_clause")

            school_team_object = create_model_object(model=SchoolTeam, high_school=high_school_object,
                                                     guardian=guardian_object, first_member=first_member_object,
                                                     second_member=second_member_object)

            if self.send_activation_link(school_team_object, request.POST.get("school_email")):
                return redirect("success_page")
        else:
            return render(request, "registration_app/registration_form.html", {
                "high_school_form": CreateHighSchoolForm(request.POST or None),
                "guardian_form": CreateGuardianForm(request.POST or None),
                "team_member_form": CreateTeamMemberForm(request.POST or None),
                "recaptcha_form": RecaptchaForm(),
                "errors": True
            })


class SuccessPageView(TemplateView):
    template_name = "registration_app/success_page.html"


class ActivateSchoolTeamView(View, SendMailToClientMixin):
    mail_subject = "Link do testu"
    email_template_name = "registration_app/test_login_page_link.html"

    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            school_team = SchoolTeam.objects.get(pk=uid)
        except:
            school_team = None

        administrators = User.objects.filter(is_superuser=True)

        if school_team is not None and account_activation_token.check_token(school_team, token):
            school_team.is_active = True
            school_team.save()
            self.send_activation_link(school_team, school_team.high_school.school_email, {"test_info": get_closest_test_by_opening_date(),
                                                                                          "uidb64": uidb64})
            return render(request, "registration_app/success_team_activation.html", {"administrators": administrators})
        else:
            return render(request, "registration_app/error_team_activation.html", {"administrators": administrators})
