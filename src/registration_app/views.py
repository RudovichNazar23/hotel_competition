from django.shortcuts import render, redirect
from django.views.generic.base import View, TemplateView
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from .forms import CreateHighSchoolForm, CreateGuardianForm, CreateTeamMemberForm
from .models import SchoolTeam


from service.mixins.get_model_by_form_field import GetModelByFormFieldMixin
from service.mixins.get_form_data_mixin import GetFormDataMixin

from service.create_model_object import create_model_object


class RegistrationView(View, GetModelByFormFieldMixin):
    template_name = "registration_app/registration_form.html"
    high_school_form = CreateHighSchoolForm()
    guardian_form = CreateGuardianForm()
    team_member_form = CreateTeamMemberForm()

    def get(self, request):
        return render(request, template_name=self.template_name, context={
            "high_school_form": self.high_school_form,
            "guardian_form": self.guardian_form,
            "team_form": self.team_member_form,
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


class CreateSchoolTeamView(View, GetFormDataMixin):
    high_school_form = CreateHighSchoolForm()
    guardian_form = CreateGuardianForm()
    team_member_form = CreateTeamMemberForm()

    def post(self, request):
        high_school_data = self.get_form_data(form_fields=self.high_school_form.fields.keys())
        guardian_form_data = self.get_form_data(form_fields=self.guardian_form.fields.keys())
        guardian_form_data.pop("guardian_clause")
        first_team_member_form_data = self.get_form_data(form_fields=self.team_member_form.fields.keys())
        first_team_member_form_data.pop("member_clause")
        second_team_member_form_data = self.get_second_team_member()

        high_school_object = create_model_object(
            model=self.high_school_form.model,
            **high_school_data
        )
        guardian_object = create_model_object(
            model=self.guardian_form.model,
            guardian_clause=request.FILES.get("guardian_clause"),
            **guardian_form_data
        )
        first_team_member_object = create_model_object(
            model=self.team_member_form.model,
            member_clause=request.FILES.get("member_clause"),
            **first_team_member_form_data
        )
        school_team = create_model_object(
            model=SchoolTeam,
            high_school=high_school_object,
            guardian=guardian_object
        )
        school_team.members.add(first_team_member_object)

        if self.check_form_data(second_team_member_form_data):
            second_team_member = create_model_object(
                model=self.team_member_form.model, member_clause=request.FILES.get("second_member_clause"), **second_team_member_form_data
            )
            school_team.members.add(second_team_member)

        return JsonResponse(
            data={
                "status": 200,
                "message": "Your team is created",
                "success_url_name": "success_page"
            },
            status=200
        ) 
    
    def get_second_team_member(self):
        second_team_member_form_data = {
            "member_name": self.request.POST.get("second_member_name"),
            "member_surname": self.request.POST.get("second_member_surname"),
        }
        return second_team_member_form_data



class SuccessPageView(TemplateView):
    template_name = "registration_app/success_page.html"
