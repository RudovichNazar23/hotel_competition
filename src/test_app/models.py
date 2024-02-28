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


class Answer(models.Model):
    class Meta:
        verbose_name_plural = "Odpowiedzi"

    answer_content = models.TextField(max_length=100, verbose_name="Treść odpowiedzi")


class Question(models.Model):
    class Meta:
        verbose_name_plural = "Pytania"

    question_content = models.TextField(max_length=100, verbose_name="Treść pytania")
    question_correct_answer = models.ForeignKey(to=Answer, related_name="correct_answer",
                                                on_delete=models.CASCADE,
                                                verbose_name="Poprawna odpowiedz"
                                                )
    question_incorrect_answers = models.ManyToManyField(to=Answer, related_name="incorrect_answers",
                                                        verbose_name="Niepoprawne odpowiedzi"
                                                        )
    question_attachment = models.FileField(upload_to="question_attachments/", blank=True,
                                           verbose_name="Załącznik dla pytania"
                                           )

    def __str__(self):
        return f"Pytanie - {self.pk}"


class Test(models.Model):
    class Meta:
        verbose_name_plural = "Testy"

    test_title = models.CharField(max_length=100, unique=True, verbose_name="Nazwa testu")
    test_creator = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="test_creator")
    test_category = models.ForeignKey(to=Category, on_delete=models.CASCADE,
                                      related_name="test_category",
                                      verbose_name="Kategoria testu"
                                      )
    test_questions = models.ManyToManyField(to=Question, related_name="test_questions")
    test_duration = models.DurationField(verbose_name="Czas wykonywania testu", default="00:00:00")
    test_date = models.DateField(verbose_name="Data otwarcia testu", unique=True)
    test_start_login_time = models.TimeField(verbose_name="Czas otwarcia logowania")
    test_end_login_time = models.TimeField(verbose_name="Czas zamknięcia logowania")

    def __str__(self):
        return f"{self.test_title}"


class Competition(models.Model):
    verbose_name_plural = "Wyniki uczęstników"

    competition_test = models.ForeignKey(to=Test, on_delete=models.CASCADE)
    competition_test_performer = models.ForeignKey(to=TeamMember, on_delete=models.CASCADE)
    competition_test_result = models.CharField(max_length=100)
    competition_test_performer_duration_time = models.DurationField(default="00:00:00")

    def __str__(self):
        return f"{self.competition_test} - {self.competition_test_performer}"

