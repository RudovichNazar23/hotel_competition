from django.db import models
from datetime import datetime


class OpenRegistration(models.Model):
    class Meta:
        verbose_name_plural = "Otwarcia rejestracji"

    date_from = models.DateField(default=datetime.now().day, verbose_name="Dzień rozpoczęcia rejestracji")
    date_to = models.DateField(default=datetime.now().day, verbose_name="Dzień zakończenia rejestracji")

    def __str__(self):
        return f"{self.date_from}"
