from ..views import RegistrationView, CreateSchoolTeamView, SuccessPageView

from service.tests.test_url_is_resolved import BaseTestUrlIsResolved


class TestUrlResolved(BaseTestUrlIsResolved):
    views = {
        "registration_page": RegistrationView,
        "create_school_team": CreateSchoolTeamView,
        "success_page": SuccessPageView
    }

    def test_test_view_is_resolved(self):
        self.parse_views()
