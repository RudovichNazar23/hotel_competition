from django.urls import path
from .views import RegistrationView

urlpatterns = [
    path("form", RegistrationView.as_view(), name="registration_page"),
]
