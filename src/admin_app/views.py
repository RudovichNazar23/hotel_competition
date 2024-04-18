from django.http import HttpResponse

from django.views.generic.list import ListView
from django.views import View

from django.contrib.auth.mixins import LoginRequiredMixin

from registration_app.models import HighSchool, Guardian, TeamMember, SchoolTeam

from service.get_filtered_model_queryset import get_filtered_model_queryset
from service.mixins.get_model_fields import get_model_fields
from service.mixins.csv_serializer_mixin import CsvSerializerMixin
from service.mixins.csv_writer import CsvWriter
from service.mixins.get_request_data import RequestObjectDataMixin
from service.mixins.add_header_mixin import HeaderMixin


class ModelsFieldListView(LoginRequiredMixin, ListView):
    template_name = "admin_app/model_field_list.html"
    extra_context = {
        **get_model_fields(model=HighSchool, context_name="high_school_fields"),
        **get_model_fields(model=Guardian, context_name="guardian_fields"),
        **get_model_fields(model=TeamMember, context_name="team_member_fields"),
    }
    queryset = []


class CreateCsvFileView(LoginRequiredMixin, View, CsvSerializerMixin, RequestObjectDataMixin, HeaderMixin):
    def post(self, request):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = "attachment; file_name=Test.csv"

        headers = self.get_form_request_values()
        self.add_header(header_list=headers)

        fields = self.get_form_request_keys()

        data = self.create_data_rows(queryset_object=get_filtered_model_queryset(model=SchoolTeam, is_active=True),
                                     fields=fields)

        writer = CsvWriter(response_object=response, headers=headers, data=data)
        writer.write_rows()

        return response

