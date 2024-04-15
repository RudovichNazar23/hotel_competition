from django.shortcuts import render

from ..get_model_object_by_uidb import get_model_object_by_uidb


class AuthorizeTeamMemberMixin:
    authorize_team_member_model = None

    def dispatch(self, request, *args, **kwargs):
        team_member = get_model_object_by_uidb(model=self.authorize_team_member_model, uidb64=request.session["member_uidb64"])
        if not team_member or "member_uidb64" not in request.session.keys():
            return render(request=request, template_name="test_app/error_test_login.html", context={
                "Error": "Brak dostępu do tej strony"
            })
        return super().dispatch(request, *args, **kwargs)
