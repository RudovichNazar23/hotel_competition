from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic.base import View

from .forms import CreateTestForm, CreateQuestionForm


class CreateTestView(LoginRequiredMixin, View):
    create_test_form = CreateTestForm()
    create_question_form = CreateQuestionForm()

    def get(self, request):
        return render(request=request, template_name="test_app/create_test.html", context={
            "create_test_form": self.create_test_form,
            "create_question_form": self.create_question_form
        })


class CreateQuestionFormObject(LoginRequiredMixin, View):
    form = CreateQuestionForm()

    def get(self, request):
        return render(request=request,
                      template_name="components/create_question_form.html",
                      context={"create_question_form": self.form}
                      )
