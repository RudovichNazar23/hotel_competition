from django.template.loader import render_to_string

from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views import View
from django.views.generic.detail import DetailView

from django.contrib.auth.mixins import LoginRequiredMixin

from registration_app.models import HighSchool, Guardian, TeamMember, SchoolTeam

from service.get_filtered_model_queryset import get_filtered_model_queryset
from service.mixins.get_model_fields import get_model_fields
from service.get_model_object import get_model_object
from service.mixins.csv_serializer_mixin import CsvSerializerMixin
from service.mixins.csv_writer import CsvWriter
from service.mixins.pdf_writer import PdfWriter
from service.mixins.get_request_data import RequestObjectDataMixin


class ModelsFieldListView(LoginRequiredMixin, ListView):
    template_name = "admin_app/model_field_list.html"
    extra_context = {
        **get_model_fields(model=HighSchool, context_name="high_school_fields"),
        **get_model_fields(model=Guardian, context_name="guardian_fields"),
        **get_model_fields(model=TeamMember, context_name="team_member_fields"),
    }
    queryset = []


class CreatePdfFileView(LoginRequiredMixin, View, CsvSerializerMixin, RequestObjectDataMixin):
    def post(self, request):
        response = HttpResponse(content_type="application/pdf")
        response["Content-Disposition"] = "attachment; filename=test.pdf"
        response["Content-Transfer-Encoding"] = "binary"

        headers = self.get_form_request_values()
        fields = self.get_form_request_keys()

        data = self.create_data_rows(queryset_object=get_filtered_model_queryset(model=SchoolTeam, is_active=True),
                                     fields=fields)

        html_string = render_to_string(template_name="admin_app/pdf_output.html", context={"headers": headers, "data": data})

        pdf_writer = PdfWriter(html_string=html_string, response_object=response)
        pdf_writer.write_data()

        return response


class CreateCsvFileView(LoginRequiredMixin, View, CsvSerializerMixin, RequestObjectDataMixin):
    def post(self, request):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = "attachment; file_name=Test.csv"

        headers = self.get_form_request_values()
        fields = self.get_form_request_keys()

        data = self.create_data_rows(queryset_object=get_filtered_model_queryset(model=SchoolTeam, is_active=True),
                                     fields=fields)

        writer = CsvWriter(response_object=response, headers=headers, data=data)
        writer.write_rows()

        return response


class NotActivatedSchoolTeamListView(LoginRequiredMixin, ListView):
    template_name = "admin_app/not_activated_school_team_list.html"
    context_object_name = "not_activated_school_teams"
    queryset = get_filtered_model_queryset(model=SchoolTeam, is_active=False)
    extra_context = {
        **get_model_fields(model=SchoolTeam, context_name="model_fields")
    }


class SchoolDetailView(LoginRequiredMixin, DetailView):
    model = HighSchool
    template_name = "admin_app/school_detail.html"
    context_object_name = "school"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["school_team"] = get_model_object(model=SchoolTeam, high_school=self.get_object())
        return context


class GuardianDetailView(LoginRequiredMixin, DetailView):
    model = Guardian
    template_name = "admin_app/guardian_detail.html"
    context_object_name = "guardian"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["guardian_school_team"] = get_model_object(model=SchoolTeam, guardian=self.get_object())
        return context


class TeamMemberDetailView(LoginRequiredMixin, DetailView):
    model = TeamMember
    template_name = "admin_app/team_member_detail.html"
    context_object_name = "team_member"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        first_member = get_model_object(model=SchoolTeam, first_member=self.get_object())
        second_member = get_model_object(model=SchoolTeam, second_member=self.get_object())
        context["team_member_school_team"] = first_member if first_member is not None else second_member
        return context
