from django.urls import path
from .views import RegistrationView, CreateSchoolTeamView

urlpatterns = [
    path("form", RegistrationView.as_view(), name="registration_page"),
    path("form/save", CreateSchoolTeamView.as_view(), name="create_school_team")
]
