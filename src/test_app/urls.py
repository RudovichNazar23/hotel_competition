from django.urls import path
from .views import TestLoginView

urlpatterns = [
    path("test_login_page/<uidb64>/<token>", TestLoginView.as_view(), name="test_login"),
]
