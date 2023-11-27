from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class HighSchool(models.Model):
    full_name = models.CharField(max_length=255, blank=False, unique=True)
    short_name = models.CharField(max_length=255, blank=False)
    city = models.CharField(max_length=255)
    post_code = models.CharField(max_length=6)
    street = models.CharField(max_length=100)
    school_mobile_phone = PhoneNumberField(region="PL", blank=False, unique=True)
    school_email = models.EmailField(blank=False, unique=True)

    def __str__(self):
        return f"{self.full_name}"


class Guardian(models.Model):
    guardian_name = models.CharField(max_length=255, blank=False)
    guardian_surname = models.CharField(max_length=255, blank=False)
    guardian_mobile_phone = PhoneNumberField(region="PL", blank=False, unique=True)
    guardian_email = models.EmailField(blank=False, unique=True)
    guardian_clause = models.FileField(upload_to="clauses/", blank=False)

    def __str__(self):
        return f"{self.guardian_name} - {self.guardian_surname}"


class TeamMember(models.Model):
    member_name = models.CharField(max_length=255, blank=True)
    member_surname = models.CharField(max_length=255, blank=True)
    member_clause = models.FileField(upload_to="clauses/", blank=False)

    def __str__(self):
        return f"{self.member_name} - {self.member_surname}"


class SchoolTeam(models.Model):
    high_school = models.ForeignKey(HighSchool, on_delete=models.CASCADE, related_name="school")
    guardian = models.ForeignKey(Guardian, on_delete=models.CASCADE)
    first_member = models.ForeignKey(TeamMember, on_delete=models.CASCADE, related_name="first_member")
    second_member = models.ForeignKey(TeamMember, on_delete=models.CASCADE, related_name="second_member", null=True)

    def __str__(self):
        return f"{self.high_school}"
