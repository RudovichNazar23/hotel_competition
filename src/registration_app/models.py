from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class HighSchool(models.Model):
    full_name = models.CharField(max_length=255, unique=True, blank=True)
    short_name = models.CharField(max_length=255, unique=True, blank=False)
    city = models.CharField(max_length=255)
    post_code = models.CharField(max_length=6)
    street = models.CharField(max_length=100)
    mobile_phone = PhoneNumberField(region="PL", unique=True, blank=True)
    email = models.EmailField(unique=True, blank=True)

    def __str__(self):
        return f"{self.full_name}"


class Guardian(models.Model):
    name = models.CharField(max_length=255, blank=True)
    surname = models.CharField(max_length=255, blank=True)
    mobile_phone = PhoneNumberField(region="PL", unique=True, blank=True)
    email = models.EmailField(unique=True, blank=True)
    clause = models.FileField(upload_to="")

    def __str__(self):
        return f"{self.name} - {self.surname}"


class TeamMember(models.Model):
    name = models.CharField(max_length=255, blank=True)
    surname = models.CharField(max_length=255, blank=True)
    clause = models.FileField(upload_to="")

    def __str__(self):
        return f"{self.name} - {self.surname}"


class SchoolTeam(models.Model):
    high_school = models.ForeignKey(HighSchool, on_delete=models.CASCADE)
    guardian = models.ForeignKey(Guardian, on_delete=models.CASCADE)
    members = models.ManyToManyField(TeamMember)

    def __str__(self):
        return f"{self.high_school}"
