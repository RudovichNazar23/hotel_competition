from django.shortcuts import render
from django.views.generic.base import View
from service.mixins.check_user import CheckUserMixin


class RegistrationView(CheckUserMixin, View):
    pass


