from django.urls import path
from .views import ActivatedSchoolTeamListView

urlpatterns = [
    path("home", ActivatedSchoolTeamListView.as_view(), name="administrator_home"),
]
