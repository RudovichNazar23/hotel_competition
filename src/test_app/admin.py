from django.contrib import admin
from django.contrib.admin import TabularInline, ModelAdmin
from .models import Category, Test, Question, Answer


class AnswerInline(TabularInline):
    model = Answer


class QuestionInline(TabularInline):
    model = Question


class QuestionAdmin(ModelAdmin):
    inlines = (AnswerInline,)


admin.site.register(Category)
admin.site.register(Test)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)

