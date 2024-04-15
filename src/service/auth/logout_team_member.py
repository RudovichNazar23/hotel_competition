from ..get_model_object_by_uidb import get_model_object_by_uidb
from registration_app.models import TeamMember
from ..get_model_object import get_model_object
from test_app.models import TeamMemberTestSession


def logout_team_member(request):
    team_member_uidb64 = request.session["member_uidb64"]
    team_member_object = get_model_object_by_uidb(model=TeamMember, uidb64=team_member_uidb64)
    team_member_session = get_model_object(model=TeamMemberTestSession, team_member=team_member_object)
    team_member_session.delete()


