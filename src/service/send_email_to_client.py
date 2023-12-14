from django.conf import settings
from .tokens import account_activation_token

from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage


class SendMailToClientMixin:
    mail_subject = None
    from_email = settings.EMAIL_HOST_USER
    email_template_name = None

    def send_activation_link(self, school_team_object, to_email):
        message = render_to_string(self.email_template_name, {
            "school_team_object": school_team_object.high_school,
            "domain": get_current_site(self.request).domain,
            "uid": urlsafe_base64_encode(force_bytes(school_team_object.pk)),
            "token": account_activation_token.make_token(school_team_object),
            "protocol": "https" if self.request.is_secure() else "http"
        })

        email = EmailMessage(self.mail_subject, message, to=[to_email])
        if email.send():
            return True
        else:
            return False
