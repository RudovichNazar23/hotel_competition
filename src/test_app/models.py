from django.db import models

from django.contrib.auth.models import User

from registration_app.models import TeamMember


class Category(models.Model):
    class Meta:
        verbose_name_plural = "Kategorie"

    category_title = models.CharField(max_length=100, unique=True, verbose_name="Nazwa kategorii")
    category_description = models.TextField(max_length=200, blank=True, verbose_name="Opis kategorii")

    def __str__(self):
        return f"{self.category_title}"


class Test(models.Model):
    class Meta:
        verbose_name_plural = "Testy"

    test_title = models.CharField(max_length=100, unique=True, verbose_name="Nazwa testu")
    test_category = models.ForeignKey(to=Category,
                                      on_delete=models.CASCADE,
                                      related_name="test_category",
                                      verbose_name="Kategoria testu")
    test_creator = models.ForeignKey(to=User,
                                     on_delete=models.CASCADE,
                                     related_name="test_creator",
                                     verbose_name="Osoba tworząca test"
                                     )
    test_duration = models.DurationField(default="00:00", verbose_name="Czas trwania testu")
    test_opening_date = models.DateField(verbose_name="Dzień otwarcia testu")
    test_start_login_time = models.TimeField(verbose_name="Godzina rozpoczęcia logowania do testu")
    test_end_login_time = models.TimeField(verbose_name="Godzina zakończenia logowania do testu")

    def __str__(self):
        return f"{self.test_title}"


class Question(models.Model):
    class Meta:
        verbose_name_plural = "Pytania"

    test = models.ForeignKey(to=Test, on_delete=models.CASCADE, verbose_name="Test")
    question_content = models.TextField(verbose_name="Treść pytania")

    def __str__(self):
        return f"{self.question_content}"


class Answer(models.Model):
    class Meta:
        verbose_name_plural = "Odpowiedzi"

    question = models.ForeignKey(to=Question, on_delete=models.CASCADE, verbose_name="Pytanie")
    answer_content = models.TextField(verbose_name="Treść odpowiedzi")
    is_correct = models.BooleanField(default=False, verbose_name="Odpowiedź jest poprawna")

    def __str__(self):
        return f"{self.question} - {self.answer_content}"


class Competition(models.Model):
    competition_test = models.ForeignKey(to=Test, on_delete=models.CASCADE)
    competition_test_performer = models.ForeignKey(to=TeamMember, on_delete=models.CASCADE)
    competition_test_result = models.CharField()
    competition_test_performer_duration_time = models.DurationField(default="00:00")

    def __str__(self):
        return f"{self.competition_test} - {self.competition_test_performer}"


