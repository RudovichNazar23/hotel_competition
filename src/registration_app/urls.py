from django.urls import path
from .views import RegistrationView, CreateSchoolTeamView, SuccessPageView, ActivateSchoolTeamView

urlpatterns = [
    path("form", RegistrationView.as_view(), name="registration_page"),
    path("form/save", CreateSchoolTeamView.as_view(), name="create_school_team"),
    path("success_page", SuccessPageView.as_view(), name="success_page"),
    path('activate/<uidb64>/<token>', ActivateSchoolTeamView.as_view(), name='activate')
]
