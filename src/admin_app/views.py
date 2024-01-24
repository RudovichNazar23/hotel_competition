from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views import View
from django.views.generic.detail import DetailView

import csv

from registration_app.models import HighSchool, Guardian, TeamMember, SchoolTeam

from service.get_filtered_model_queryset import get_filtered_model_queryset
from service.mixins.get_model_fields import get_model_fields
from service.get_model_object import get_model_object
from service.mixins.test_mixin import TestMixin


class ModelsFieldListView(ListView):
    template_name = "admin_app/activated_school_team_list.html"
    context_object_name = "activated_school_teams"
    extra_context = {
        **get_model_fields(model=HighSchool, context_name="high_school_fields"),
        **get_model_fields(model=Guardian, context_name="guardian_fields"),
        **get_model_fields(model=TeamMember, context_name="team_member_fields"),
    }
    queryset = get_filtered_model_queryset(model=SchoolTeam, is_active=True)


class CreatePdfFileView(View):
    pass


class CreateCsvFileView(View, TestMixin):
    def post(self, request):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = "attachment; file_name=Test.csv"

        writer = csv.writer(response)
        writer.writerow([*filter(lambda x: x, [*request.POST.values()][1:])])

        fields = [*filter(lambda x: x, [*request.POST.keys()][1:])]

        high_school_data = self.get_model_value_list(obj=self.get_model_fields(model=HighSchool, fields=fields))
        guardian_data = self.get_model_value_list(obj=self.get_model_fields(model=Guardian, fields=fields))
        team_member_data = self.get_model_value_list(obj=self.get_model_fields(model=TeamMember, fields=fields))

        data = self.create_data_rows(high_school_data, guardian_data, team_member_data)

        for row in data:
            writer.writerow(row)

        return response


class NotActivatedSchoolTeamListView(ListView):
    template_name = "admin_app/not_activated_school_team_list.html"
    context_object_name = "not_activated_school_teams"
    queryset = get_filtered_model_queryset(model=SchoolTeam, is_active=False)
    extra_context = {
        **get_model_fields(model=SchoolTeam, context_name="model_fields")
    }


class SchoolDetailView(DetailView):
    model = HighSchool
    template_name = "admin_app/school_detail.html"
    context_object_name = "school"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["school_team"] = get_model_object(model=SchoolTeam, high_school=self.get_object())
        return context


class GuardianDetailView(DetailView):
    model = Guardian
    template_name = "admin_app/guardian_detail.html"
    context_object_name = "guardian"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["guardian_school_team"] = get_model_object(model=SchoolTeam, guardian=self.get_object())
        return context


class TeamMemberDetailView(DetailView):
    model = TeamMember
    template_name = "admin_app/team_member_detail.html"
    context_object_name = "team_member"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        first_member = get_model_object(model=SchoolTeam, first_member=self.get_object())
        second_member = get_model_object(model=SchoolTeam, second_member=self.get_object())
        context["team_member_school_team"] = first_member if first_member is not None else second_member
        return context
