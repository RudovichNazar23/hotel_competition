# Generated by Django 4.2.6 on 2024-03-08 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0003_alter_question_question_correct_answer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_correct_answer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='correct_answer', to='test_app.answer', verbose_name='Poprawna odpowiedz'),
        ),
    ]