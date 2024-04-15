from django.shortcuts import render

from ..get_model_object import get_model_object
from ..get_model_object_by_uidb import get_model_object_by_uidb
from registration_app.models import TeamMember

from test_app.models import Competition


class CompetitionResultPermissionsMixin:
    def dispatch(self, request, pk, member_uidb64):
        team_member = get_model_object_by_uidb(model=TeamMember, uidb64=member_uidb64)
        competition_result = get_model_object(model=Competition, pk=pk)
        if team_member != competition_result.competition_test_performer:
            return render(request=request, template_name="test_app/error_test_login.html", context={
                "Error": "Brak dostępu do tej strony"
            })
        else:
            return super().dispatch(request, pk, member_uidb64)
