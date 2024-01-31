from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class HighSchool(models.Model):
    class Meta:
        verbose_name_plural = "Szkoły"

    full_name = models.CharField(max_length=255, blank=False, unique=True, verbose_name="Pełna nazwa szkoły")
    short_name = models.CharField(max_length=255, blank=True, verbose_name="Nazwa w skrócie")
    city = models.CharField(max_length=255, verbose_name="Miasto")
    post_code = models.CharField(max_length=6, verbose_name="Kod pocztowy")
    street = models.CharField(max_length=100, verbose_name="Ulica")
    school_mobile_phone = PhoneNumberField(region="PL", blank=False, unique=True, verbose_name="Telefon komórkowy szkoły")
    school_email = models.EmailField(blank=False, unique=True, verbose_name="E-mail szkoły")

    def __str__(self):
        return f"{self.full_name}"


class Guardian(models.Model):
    class Meta:
        verbose_name_plural = "Opiekunowie"

    guardian_name = models.CharField(max_length=255, verbose_name="Imie opiekuna")
    guardian_surname = models.CharField(max_length=255, verbose_name="Nazwisko opiekuna")
    guardian_mobile_phone = PhoneNumberField(region="PL", blank=False, unique=True, verbose_name="Telefon komórkowy opiekuna")
    guardian_email = models.EmailField(blank=True, unique=True, verbose_name="E-mail opiekuna")
    guardian_clause = models.FileField(upload_to="clauses/", blank=False, verbose_name="Klauzula opiekuna")

    def __str__(self):
        return f"{self.guardian_name} {self.guardian_surname}"


class TeamMember(models.Model):
    class Meta:
        verbose_name_plural = "Uczniowie"

    member_name = models.CharField(max_length=255, verbose_name="Imie uczęstnika")
    member_surname = models.CharField(max_length=255, verbose_name="Nazwisko uczęstnika")
    member_clause = models.FileField(upload_to="clauses/", blank=False, verbose_name="Klauzula uczęstnika")

    def __str__(self):
        return f"{self.member_name} {self.member_surname}"


class SchoolTeam(models.Model):
    class Meta:
        verbose_name_plural = "Zespoły szkolne"

    high_school = models.ForeignKey(HighSchool, on_delete=models.CASCADE, related_name="school", verbose_name="Nazwa szkoły")
    guardian = models.ForeignKey(Guardian, on_delete=models.CASCADE, verbose_name="Opiekun")
    first_member = models.ForeignKey(TeamMember, on_delete=models.CASCADE, related_name="first_member", verbose_name="Pierwszy uczęstnik")
    second_member = models.ForeignKey(TeamMember, on_delete=models.CASCADE, related_name="second_member", null=True, blank=True, verbose_name="Drugi uczęstnik")
    is_active = models.BooleanField(default=False, blank=True, verbose_name="Zespół aktywny")

    def __str__(self):
        return f"{self.high_school}"
