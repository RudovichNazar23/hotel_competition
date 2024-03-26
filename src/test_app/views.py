from django.shortcuts import render, redirect
from django.urls import reverse

from django.views.generic.base import View

from .models import Test, Question, Competition, Answer
from .forms import TestLoginForm

from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes

from service.get_closest_test import get_closest_test_by_opening_date
from service.authenticate_team_member import authenticate_team_member
from service.get_model_object_by_uidb import get_model_object_by_uidb
from service.get_model_object import get_model_object
from service.get_filtered_model_queryset import get_filtered_model_queryset
from service.create_model_object import create_model_object
from service.count_test_result import count_test_result

from service.mixins.check_opened_test import CheckOpenedTestMixin
from service.mixins.authorize_team_member_mixin import AuthorizeTeamMemberMixin
from service.mixins.get_request_data import RequestObjectDataMixin

from registration_app.models import SchoolTeam
from registration_app.models import TeamMember


class TestLoginView(CheckOpenedTestMixin, View):
    template_name = "test_app/test_login.html"
    context = {
        "form": TestLoginForm()
    }

    def get(self, request, uidb64):
        school_team = get_model_object_by_uidb(model=SchoolTeam, uidb64=uidb64)
        if not school_team:
            return render(request=request, template_name="test_app/error_test_login_page.html", context={})

        self.context["uidb64"] = uidb64
        self.context["school_team"] = school_team
        return render(request=request, template_name=self.template_name, context=self.context)

    def post(self, request, uidb64):
        school_team = get_model_object_by_uidb(model=SchoolTeam, uidb64=uidb64)
        test = get_closest_test_by_opening_date()
        form = TestLoginForm(request.POST)

        if form.is_valid() and school_team is not None:
            member_name = form.cleaned_data.get("member_name")
            member_surname = form.cleaned_data.get("member_surname")

            team_member = authenticate_team_member(school_team_object=school_team, name=member_name,
                                                   surname=member_surname)
            if team_member:
                pk = urlsafe_base64_encode(force_bytes(team_member.pk))
                request.session["member_uidb64"] = pk
                return redirect(reverse("test_detail", kwargs={"member_uidb64": pk, "test_title": test}))
        return render(request=request, template_name=self.template_name, context={
            "error_message": "Imię albo nazwisko nie jest zgodne ",
            "uidb64": uidb64,
            "form": form
        })


class TestDetailView(AuthorizeTeamMemberMixin, View, RequestObjectDataMixin):
    authorize_team_member_model = TeamMember

    def get(self, request, member_uidb64, test_title):
        test = get_model_object(model=Test, test_title=test_title)
        test_questions = get_filtered_model_queryset(model=Question, test=test)
        return render(request=request, template_name="test_app/test_detail.html", context={
            "test": test,
            "test_questions": test_questions,
        })

    def post(self, request, member_uidb64, test_title):
        team_member = get_model_object_by_uidb(model=TeamMember, uidb64=member_uidb64)
        test = get_model_object(model=Test, test_title=test_title)

        answers = [get_model_object(model=Answer, answer_content=i) for i in self.get_form_request_values()]

        competition_test_result = count_test_result(answers=answers)

        competition_object = create_model_object(model=Competition,
                                                 competition_test=test,
                                                 competition_test_performer=team_member,
                                                 competition_test_result=competition_test_result,
                                                 competition_test_performer_duration_time="01:00:00"
                                                 )
        return redirect("competition_result")


class CompetitionResultDetailView(View):
    template_name = "test_app/competition_result.html"

    def get(self, request):
        return render(request=request, template_name=self.template_name, context={})
