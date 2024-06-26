from django.urls import path
from .views import TestLoginView, TestDetailView, CompetitionResultDetailView

urlpatterns = [
    path("test_login_page/<uidb64>/<token>", TestLoginView.as_view(), name="test_login"),
    path("test_detail/<member_uidb64>/<test_title>", TestDetailView.as_view(), name="test_detail"),
    path("competition_result/<member_uidb64>/<int:pk>", CompetitionResultDetailView.as_view(), name="competition_result")
]
