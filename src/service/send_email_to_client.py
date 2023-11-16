from django.core.mail import send_mail
from django.conf import settings


def send_email_to_client(clients: list, message: str):
    send_mail(
        subject="Competition registration",
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=clients,
        fail_silently=False
    )
