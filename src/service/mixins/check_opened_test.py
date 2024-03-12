from datetime import date
from datetime import datetime

from django.shortcuts import render

from service.get_closest_test import get_closest_test_by_opening_date


class CheckOpenedTestMixin:
    def dispatch(self, request, *args, **kwargs):
        test = get_closest_test_by_opening_date()
        if (self.get_current_date() != test.test_opening_date or
                not test.test_start_login_time <= self.get_current_time() <= test.test_end_login_time):
            return render(request=request, template_name="test_app/test_is_closed.html", context={"test": test})
        else:
            return super().dispatch(request, *args, **kwargs)

    @staticmethod
    def get_current_date():
        return date.today()

    @staticmethod
    def get_current_time():
        return datetime.now().time()
