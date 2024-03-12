import datetime
from datetime import timedelta
from test_app.models import Test

from .get_all_model_objects import get_all_model_objects


def get_closest_test_by_opening_date():
    all_tests = get_all_model_objects(model=Test)
    current_date = datetime.date.today()

    greater = all_tests.filter(test_opening_date__gte=current_date).order_by("test_opening_date").first()
    less = all_tests.filter(test_opening_date__lte=current_date).order_by("-test_opening_date").first()

    if greater and less:
        return greater if abs(greater.test_opening_date - current_date) < abs(
            less.test_opening_date - current_date) else less
    else:
        return greater or less
