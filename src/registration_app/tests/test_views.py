from django.test import TestCase, Client
from django.urls import reverse
from ..models import HighSchool


class TestRegistrationView(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse("registration_page")
        self.school1_object = HighSchool.objects.create(full_name="School1",
                                                        short_name="schl1",
                                                        city="Slupsk",
                                                        post_code="200",
                                                        street="dluga25",
                                                        school_mobile_phone="+48576134323",
                                                        school_email="school1@gmail.com"
                                                        )

    def test_registration_page_GET(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "registration_app/registration_form.html")
        self.assertIn("high_school_form", response.context.keys())
        self.assertIn("guardian_form", response.context.keys())
        self.assertIn("team_member_form", response.context.keys())

        print("Test 1 - Success")

    def test_registration_page_POST(self):
        response = self.client.post(path=self.url, data={"field_name": "full_name", "field_value": self.school1_object.full_name})
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.json()["status"], 400)
        self.assertIn("message", response.json())

        print("Test 2 - Success")
