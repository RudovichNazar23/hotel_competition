from django.shortcuts import redirect
from .mixins.check_user import CheckUserMixin
from django.views.generic.base import View


class RedirectView(CheckUserMixin, View):
    pass
