from django.urls import path
from .views import (
    ModelsFieldListView,
    NotActivatedSchoolTeamListView,
    CreateCsvFileView,
    SchoolDetailView,
    GuardianDetailView,
    TeamMemberDetailView,
    OpenRegistrationView
)

urlpatterns = [
    path("models_field_list", ModelsFieldListView.as_view(), name="models_field_list"),
    path("not_activated_school_teams", NotActivatedSchoolTeamListView.as_view(), name="not_activated_school_teams"),
    path("create_csv_file", CreateCsvFileView.as_view(), name="create_csv_file"),
    path("school_detail/<int:pk>", SchoolDetailView.as_view(), name="school_detail"),
    path("guardian_detail/<int:pk>", GuardianDetailView.as_view(), name="guardian_detail"),
    path("team_member_detail/<int:pk>", TeamMemberDetailView.as_view(), name="team_member_detail"),
    path("open_registration", OpenRegistrationView.as_view(), name="open_registration")
]
