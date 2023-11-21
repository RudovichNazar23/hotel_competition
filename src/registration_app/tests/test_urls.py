from django.test import SimpleTestCase
from django.urls import resolve, reverse

from ..views import RegistrationView, CreateSchoolTeamView, SuccessPageView


class TestUrlResolved(SimpleTestCase):
    def assert_url_resolves_to_view(self, reverse_name: str, expected_view):
        url = reverse(reverse_name)
        self.assertEquals(resolve(url).func.view_class, expected_view)

    def test_form_url_is_resolved(self):
        self.assert_url_resolves_to_view(reverse_name="registration_page", expected_view=RegistrationView)

    def test_create_school_team_is_resolved(self):
        self.assert_url_resolves_to_view(reverse_name="create_school_team", expected_view=CreateSchoolTeamView)

    def test_success_page_is_resolved(self):
        self.assert_url_resolves_to_view(reverse_name="success_page", expected_view=SuccessPageView)

