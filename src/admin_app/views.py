from django.shortcuts import render
from django.views.generic.list import ListView

from registration_app.models import SchoolTeam

from service.get_filtered_model_queryset import get_filtered_model_queryset


class ActivatedSchoolTeamListView(ListView):
    template_name = "admin_app/activated_school_team_list.html"
    context_object_name = "activated_school_teams"
    queryset = get_filtered_model_queryset(model=SchoolTeam, is_active=True)


class NotActivatedSchoolTeamListView(ListView):
    template_name = ""
    context_object_name = ""
