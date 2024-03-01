from django.urls import path
from .views import CreateTestView, CreateQuestionFormObject

urlpatterns = [
    path("create_test", CreateTestView.as_view(), name="create_test"),
    path("create_question_form", CreateQuestionFormObject.as_view(), name="create_question_form"),
]
