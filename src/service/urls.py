from django.urls import path
from .views import RedirectView

urlpatterns = [
    path("", RedirectView.as_view(), name="redirect_view"),
]
