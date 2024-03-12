from django.http import Http404
from django.shortcuts import render
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode

from registration_app.models import SchoolTeam

from service.tokens import account_activation_token


class ActivateSchoolMixin:
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
            self.context["school_team"] = school_team
            return super().dispatch(request, uidb64, token)
        else:
            return render(request=request, template_name="error_link.html", context={self.error_context})
