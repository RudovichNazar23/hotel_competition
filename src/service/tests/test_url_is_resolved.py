from django.test import SimpleTestCase
from django.urls import reverse, resolve


class BaseTestUrlIsResolved(SimpleTestCase):
    views = {

    }

    def assert_url_is_resolved(self, reverse_name: str, expected_view):
        url = reverse(reverse_name)
        self.assertEquals(resolve(url).func.view_class, expected_view)
        print(f"{url} matches with {expected_view}")

    def parse_views(self):
        if not self.views:
            raise AttributeError("views attribute is empty")

        for reverse_name in self.views:
            self.assert_url_is_resolved(reverse_name=reverse_name, expected_view=self.views[reverse_name])
