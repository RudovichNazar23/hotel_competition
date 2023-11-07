from django.urls import path
from .views import RegistrationView, CreateSchoolTeamView, SuccessPageView

urlpatterns = [
    path("form", RegistrationView.as_view(), name="registration_page"),
    path("form/save", CreateSchoolTeamView.as_view(), name="create_school_team"),
    path("success_page", SuccessPageView.as_view(), name="success_page"),
]
