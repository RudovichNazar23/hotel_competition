from django.urls import path
from .views import ActivatedSchoolTeamListView, NotActivatedSchoolTeamListView

urlpatterns = [
    path("activated_school_teams", ActivatedSchoolTeamListView.as_view(), name="activated_school_teams"),
    path("not_activated_school_teams", NotActivatedSchoolTeamListView.as_view(), name="not_activated_school_teams")
]
