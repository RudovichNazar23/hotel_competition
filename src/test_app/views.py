from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode

from django.views.generic.base import View

from .forms import TestLoginForm

from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes

from service.get_closest_test import get_closest_test_by_opening_date
from service.authenticate_team_member import authenticate_team_member
from service.get_model_object import get_model_object

from service.mixins.check_opened_test import CheckOpenedTestMixin

from registration_app.models import SchoolTeam


class TestLoginView(CheckOpenedTestMixin, View):
    template_name = "test_app/test_login.html"
    context = {
        "form": TestLoginForm()
    }

    def get(self, request, uidb64):
        school_team_pk = force_str(urlsafe_base64_decode(uidb64))
        school_team = get_model_object(model=SchoolTeam, pk=school_team_pk)
        self.context["uidb64"] = uidb64

        if not school_team:
            return render(request=request, template_name="test_app/error_test_login_page.html", context={})
        self.context["school_team"] = school_team
        return render(request=request, template_name=self.template_name, context=self.context)

    def post(self, request, uidb64):
        school_team_pk = force_str(urlsafe_base64_decode(uidb64))
        school_team = get_model_object(model=SchoolTeam, pk=school_team_pk)
        test = get_closest_test_by_opening_date()
        form = TestLoginForm(request.POST)

        if form.is_valid() and school_team is not None:
            member_name = form.cleaned_data.get("member_name")
            member_surname = form.cleaned_data.get("member_surname")

            team_member = authenticate_team_member(school_team_object=school_team, name=member_name, surname=member_surname)
            if team_member:
                pk = urlsafe_base64_encode(force_bytes(team_member.pk))
                return redirect(reverse("test_detail", kwargs={"member_uidb64": pk, "test_title": test}))
        return render(request=request, template_name=self.template_name, context={
                "error_message": "Imię albo nazwisko nie jest zgodne ",
                "uidb64": uidb64,
                "form": form
            })


class TestDetailView(View):
    def get(self, request, member_uidb64, test_title):
        return render(request=request, template_name="test_app/test_detail.html")
