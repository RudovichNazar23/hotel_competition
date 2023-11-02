from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.http import JsonResponse

from .forms import CreateHighSchoolForm, CreateGuardianForm, CreateTeamMemberForm
from service.mixins.get_model_by_form_field import GetModelByFormFieldMixin
from service.get_object import get_model_object


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
        obj = get_model_object(model=model, field_name=field_value)
        if obj:
            return JsonResponse(
                data={
                    "status": 400,
                    "message": "Object with this data already exists"
                },
                status=200
            )
        else:
            return JsonResponse(
                data={
                    "status": 200,
                    "message": "Ok!"
                },
                status=200
            )
