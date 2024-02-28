from django.contrib import admin
from .models import Category, Answer, Question, Test, Competition

admin.site.register(Category)
admin.site.register(Answer)
admin.site.register(Question)
admin.site.register(Test)
admin.site.register(Competition)
