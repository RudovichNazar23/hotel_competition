from django.urls import path
from .views import TestLoginView, TestDetailView

urlpatterns = [
    path("test_login_page/<uidb64>", TestLoginView.as_view(), name="test_login"),
    path("test_detail/<member_uidb64>/<test_title>", TestDetailView.as_view(), name="test_detail"),
]
