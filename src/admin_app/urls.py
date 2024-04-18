from django.urls import path
from .views import (
    ModelsFieldListView,
    CreateCsvFileView,
)

urlpatterns = [
    path("models_field_list", ModelsFieldListView.as_view(), name="models_field_list"),
    path("create_csv_file", CreateCsvFileView.as_view(), name="create_csv_file"),
]
