from django.urls import path
from .views import ModelsFieldListView, NotActivatedSchoolTeamListView, CreatePdfFileView, CreateCsvFileView

urlpatterns = [
    path("models_field_list", ModelsFieldListView.as_view(), name="models_field_list"),
    path("not_activated_school_teams", NotActivatedSchoolTeamListView.as_view(), name="not_activated_school_teams"),
    path("create_pdf_file", CreatePdfFileView.as_view(), name="create_pdf_file"),
    path("create_csv_file", CreateCsvFileView.as_view(), name="create_csv_file"),
]
