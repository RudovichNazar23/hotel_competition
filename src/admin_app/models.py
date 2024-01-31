from django.db import models


class OpenRegistration(models.Model):
    class Meta:
        verbose_name_plural = "Otwarcia rejestracji"

    date = models.DateField(verbose_name="Data")
    time_from = models.TimeField(verbose_name="Czas pozpoczęcia rejestracji")
    time_to = models.TimeField(verbose_name="Czas zakończenia rejestracji")

    def __str__(self):
        return f"{self.date}"
