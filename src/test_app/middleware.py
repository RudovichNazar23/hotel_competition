from django.contrib.sessions.middleware import SessionMiddleware
from django.urls import resolve
from django.shortcuts import render
from test_app.models import TeamMemberTestSession

from service.get_model_object_by_uidb import get_model_object_by_uidb

from registration_app.models import TeamMember


class PreventMultipleSessionMiddleware(SessionMiddleware):
    def process_request(self, request):
        ALLOWED_ROUTE = "test/test_detail/<member_uidb64>/<test_title>"

        resolved_view = resolve(request.path_info)

        if resolved_view.route == ALLOWED_ROUTE:
            if request.method == "GET":
                if "member_uidb64" in request.session.keys():
                    team_member = get_model_object_by_uidb(model=TeamMember, uidb64=request.session["member_uidb64"])

                    team_member_session = None

                    try:
                        team_member_session = TeamMemberTestSession.objects.get(team_member=team_member)
                    except Exception as e:
                        pass

                    if team_member_session and team_member_session.team_member_client != request.META["HTTP_USER_AGENT"]:
                        return render(request, "test_app/error_test_login.html", {"Error": "Ten użytkownik już jest zalogowany"})
                    if not team_member_session:
                        TeamMemberTestSession.objects.create(team_member=team_member, member_uidb64=request.session["member_uidb64"], team_member_client=request.META["HTTP_USER_AGENT"])
        super().process_request(request)
