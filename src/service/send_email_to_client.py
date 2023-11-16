from django.core.mail import send_mass_mail
from django.conf import settings


class SendMailToClientMixin:
    subject = None
    message_body = None
    from_email = settings.EMAIL_HOST_USER

    def send_email_to_client(self, messages: tuple):
        send_mass_mail(datatuple=messages, fail_silently=False)

    def create_message(self, email_to: str):
        message = (self.subject, self.message_body, self.from_email, [email_to])
        return message
