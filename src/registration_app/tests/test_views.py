from django.test import TestCase, Client
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
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

        print({self.__class__.__name__: "Test1", "result": "success"})

    def test_registration_page_POST(self):
        response = self.client.post(path=self.url, data={"field_name": "full_name", "field_value": self.school1_object.full_name})
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.json()["status"], 400)
        self.assertIn("message", response.json())

        print({self.__class__.__name__: "Test2", "result": "success"})


class TestCreateSchoolTeamView(TestCase):
    def setUp(self):
        self.client = Client()
        self.guardian_clause = SimpleUploadedFile("guardian.txt", b"file_content")
        self.member1_clause = SimpleUploadedFile("member1.txt", b"file_content")
        self.url = reverse("create_school_team")
        self.form_correct_data = {
            "full_name": "School1",
            "short_name": "schl1",
            "city": "Warszawa",
            "post_code": "10-200",
            "street": "Wiejska 20",
            "school_mobile_phone": "+48576134323",
            "school_email": "school1@gmail.com",
            "guardian_name": "Karol",
            "guardian_surname": "Siatka",
            "guardian_mobile_phone": "+48576115323",
            "guardian_email": "guard1@gmail.com",
            "member_name": "Nazar",
            "member_surname": "Rudovich",
            "member_clause": self.guardian_clause,
            "guardian_clause": self.member1_clause,
        }
        self.form_incorrect_data = {
            "full_name": "School2",
            "short_name": "schl1",
            "city": "Warszawa",
            "post_code": "10-200",
            "street": "Wiejska 20",
            "school_mobile_phone": "dfnvjbdbjvdfnvbdfn",
            "school_email": "school2gmail",
            "guardian_name": "Karol",
            "guardian_surname": "Siatka",
            "guardian_mobile_phone": "+4857",
            "guardian_email": "guard2@gmailcom",
            "member_name": "Steve",
            "member_surname": "Jobs",
            "member_clause": self.member1_clause,
            "guardian_clause": self.guardian_clause
        }

    def test_GET_request(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 405)

        print({self.__class__.__name__: "Test1", "result": "success"})

    def test_correct_data_saving(self):
        response = self.client.post(path=self.url, data=self.form_correct_data)
        self.assertIn("status", response.json())
        self.assertEquals(response.json()["status"], 200)

        print({self.__class__.__name__: "Test2", "result": "success"})

    def test_incorrect_data_saving(self):
        response = self.client.post(path=self.url, data=self.form_incorrect_data)
        self.assertEquals(response.json()["status"], 400)
        print({self.__class__.__name__: "Test", "result": "success"})
