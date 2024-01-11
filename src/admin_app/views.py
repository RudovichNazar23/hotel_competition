from django.views.generic.list import ListView
from django.views import View


from registration_app.models import HighSchool, Guardian, TeamMember, SchoolTeam

from service.get_filtered_model_queryset import get_filtered_model_queryset
from service.mixins.get_model_fields import get_model_fields


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
    def post(self, request):
        pass


class CreateCsvFileView(View):
    pass


class NotActivatedSchoolTeamListView(ListView):
    template_name = "admin_app/not_activated_school_team_list.html"
    context_object_name = "not_activated_school_teams"
    queryset = get_filtered_model_queryset(model=SchoolTeam, is_active=False)
