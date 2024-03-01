from django import forms
from .models import Test, Question, Answer

from durationwidget.widgets import TimeDurationWidget


class CreateTestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = (
            "test_title",
            "test_category",
            "test_duration",
            "test_date",
            "test_start_login_time",
            "test_end_login_time"
        )

        widgets = {
            "test_title": forms.TextInput(attrs={"class": "form-control"}),
            "test_category": forms.TextInput(attrs={"class": "form-control"}),
            "test_duration": TimeDurationWidget(show_hours=True,
                                                show_minutes=True,
                                                show_days=False,
                                                show_seconds=False,
                                                attrs={"class": "form-control"}
                                                ),
            "test_date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "test_start_login_time": forms.TimeInput(attrs={"type": "time", "class": "form-control"}),
            "test_end_login_time": forms.TimeInput(attrs={"type": "time", "class": "form-control"})
        }


class CreateQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ("question_content", "question_correct_answer", "question_attachment",)

        widgets = {
            "question_content": forms.Textarea(attrs={"class": "form-control"}),
            "question_attachment": forms.FileInput(attrs={"class": "form-control"}),
            "question_correct_answer": forms.Textarea(attrs={"class": "form-control"})
        }
