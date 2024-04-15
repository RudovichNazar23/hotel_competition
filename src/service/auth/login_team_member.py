from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes


def login_team_member(request, team_member):
    pk = urlsafe_base64_encode(force_bytes(team_member.pk))
    request.session["member_uidb64"] = pk
