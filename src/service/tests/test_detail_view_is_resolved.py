from django.urls import reverse, resolve

from .test_url_is_resolved import BaseTestUrlIsResolved


class BaseTestDetailViewIsResolved(BaseTestUrlIsResolved):
    views = {

    }

    kwargs = {

    }

    def assert_url_is_resolved(self, reverse_name: str, expected_view):
        if not self.kwargs:
            raise AttributeError("Class attribute kwargs is empty")

        url = reverse(reverse_name, kwargs=self.kwargs)
        self.assertEquals(resolve(url).func.view_class, expected_view)
        print(f"{url} matches with {expected_view}")


