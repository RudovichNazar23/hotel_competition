from django.contrib import admin
from django.contrib.admin import TabularInline, ModelAdmin
from .models import Category, Test, Question, Answer, Competition


class AnswerInline(TabularInline):
    model = Answer


class QuestionInline(TabularInline):
    model = Question


class QuestionAdmin(ModelAdmin):
    inlines = (AnswerInline,)


class TestAdmin(ModelAdmin):
    list_display = ("test_title", "test_category", "test_creator", "test_duration", "test_opening_date", "test_start_login_time", "test_end_login_time")
    list_filter = ("test_category", "test_opening_date")


class CompetitionAdmin(ModelAdmin):
    list_display = ("competition_test", "competition_test_performer", "competition_test_result", "competition_test_performer_duration_time")
    list_filter = ("competition_test_result", "competition_test_performer_duration_time")


admin.site.register(Category)
admin.site.register(Test, TestAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(Competition, CompetitionAdmin)

