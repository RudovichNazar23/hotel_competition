from service.tests.test_url_is_resolved import BaseTestUrlIsResolved
from service.tests.test_detail_view_is_resolved import BaseTestDetailViewIsResolved

from ..views import (
    ModelsFieldListView,
    CreatePdfFileView,
    CreateCsvFileView,
    NotActivatedSchoolTeamListView,
    SchoolDetailView,
    GuardianDetailView,
    TeamMemberDetailView,
    OpenRegistrationView
)


class TestUrlIsResolved(BaseTestUrlIsResolved):
    views = {
        "models_field_list": ModelsFieldListView,
        "not_activated_school_teams": NotActivatedSchoolTeamListView,
        "create_pdf_file": CreatePdfFileView,
        "create_csv_file": CreateCsvFileView,
        "open_registration": OpenRegistrationView,
    }

    def test_view_is_resolved(self):
        self.parse_views()


class TestDetailViewUrlIsResolved(BaseTestDetailViewIsResolved):
    views = {
        "school_detail": SchoolDetailView,
        "guardian_detail": GuardianDetailView,
        "team_member_detail": TeamMemberDetailView,
    }

    kwargs = {
        "pk": 1
    }

    def test_detail_view_url_is_resolved(self):
        self.parse_views()
