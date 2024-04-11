from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from service.create_model_object import create_model_object


def login_team_member(request, team_member, session_model):
    pk = urlsafe_base64_encode(force_bytes(team_member.pk))
    request.session["member_uidb64"] = pk
