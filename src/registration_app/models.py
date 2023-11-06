from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class HighSchool(models.Model):
    full_name = models.CharField(max_length=255, unique=True, blank=False)
    short_name = models.CharField(max_length=255, unique=True, blank=False)
    city = models.CharField(max_length=255)
    post_code = models.CharField(max_length=6)
    street = models.CharField(max_length=100)
    school_mobile_phone = PhoneNumberField(region="PL", unique=True, blank=False)
    school_email = models.EmailField(unique=True, blank=False)

    def __str__(self):
        return f"{self.full_name}"


class Guardian(models.Model):
    guardian_name = models.CharField(max_length=255, blank=False)
    guardian_surname = models.CharField(max_length=255, blank=False)
    guardian_mobile_phone = PhoneNumberField(region="PL", unique=True, blank=False)
    guardian_email = models.EmailField(unique=True, blank=False)
    guardian_clause = models.FileField(upload_to="clauses/", blank=True)

    def __str__(self):
        return f"{self.guardian_name} - {self.guardian_surname}"


class TeamMember(models.Model):
    member_name = models.CharField(max_length=255, blank=True)
    member_surname = models.CharField(max_length=255, blank=True)
    member_clause = models.FileField(upload_to="clauses/", blank=True)

    def __str__(self):
        return f"{self.member_name} - {self.member_surname}"


class SchoolTeam(models.Model):
    high_school = models.ForeignKey(HighSchool, on_delete=models.CASCADE)
    guardian = models.ForeignKey(Guardian, on_delete=models.CASCADE)
    members = models.ManyToManyField(TeamMember)

    def __str__(self):
        return f"{self.high_school}"
