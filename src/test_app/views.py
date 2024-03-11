from django.shortcuts import render, redirect
from django.urls import reverse

from django.views.generic.base import View

from .forms import TestLoginForm

from service.mixins.activate_school_mixin import ActivateSchoolMixin


class TestLoginView(ActivateSchoolMixin, View):
    template_name = "test_app/test_login.html"
    error_template_name = "test_app/error_test_login.html"
    context = {
        "login_form": TestLoginForm()
    }

    def post(self, request, *args, **kwargs):
        pass
