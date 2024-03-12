from datetime import date
from datetime import datetime
from django.shortcuts import render, redirect

from django.views.generic.base import View

from .forms import TestLoginForm

from service.mixins.activate_school_mixin import ActivateSchoolMixin
from service.mixins.check_opened_test import CheckOpenedTestMixin
from service.get_closest_test import get_closest_test_by_opening_date


class TestLoginView(ActivateSchoolMixin, CheckOpenedTestMixin, View):
    template_name = "test_app/test_login.html"
    context = {
        "login_form": TestLoginForm()
    }

    def get(self, request, uidb64, token):
        test = get_closest_test_by_opening_date()
        self.context["test"] = test
        return render(request=request, template_name=self.template_name, context=self.context)

    def post(self, request, *args, **kwargs):
        pass
