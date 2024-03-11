from django.shortcuts import render
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode

from registration_app.models import SchoolTeam

from service.tokens import account_activation_token


class ActivateSchoolMixin:
    template_name = None
    error_template_name = None
    context = {}
    error_context = {}

    def dispatch(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            school_team = SchoolTeam.objects.get(pk=uid)
        except Exception as ex:
            school_team = None

        if school_team is not None and account_activation_token.check_token(school_team, token):
            return render(request=request, template_name=self.template_name, context=self.context)
        else:
            return render(request=request, template_name=self.error_template_name, context=self.error_context)
