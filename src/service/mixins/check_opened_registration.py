from django.shortcuts import render

from ..get_model_object import get_model_object
from datetime import date, datetime

from admin_app.models import OpenRegistration


class CheckOpenedRegistrationMixin:
    error_template_name = ""
    error_context_data = {}

    def dispatch(self, request, *args, **kwargs):
        registration_is_active = self.registration_is_active()

        if not registration_is_active:
            return render(request=request, template_name=self.error_template_name, context=self.error_context_data)
        return super().dispatch(request, *args, **kwargs)

    @staticmethod
    def get_current_time():
        return datetime.now().time()

    @staticmethod
    def get_current_date():
        return date.today()

    def registration_is_active(self):
        current_date = self.get_current_date()
        current_time = self.get_current_time()

        model_object = get_model_object(model=OpenRegistration, date=current_date)

        if not model_object or not model_object.time_from <= current_time <= model_object.time_to:
            return False
        return True
