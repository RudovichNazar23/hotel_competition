# Generated by Django 4.2.6 on 2024-03-21 08:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('test_app', '0006_test_question_competition_answer'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'verbose_name_plural': 'Odpowiedzi'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name_plural': 'Pytania'},
        ),
        migrations.AlterModelOptions(
            name='test',
            options={'verbose_name_plural': 'Testy'},
        ),
        migrations.AlterField(
            model_name='answer',
            name='answer_content',
            field=models.TextField(verbose_name='Treść odpowiedzi'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='is_correct',
            field=models.BooleanField(default=False, verbose_name='Odpowiedź jest poprawna'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_app.question', verbose_name='Pytanie'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_content',
            field=models.TextField(verbose_name='Treść pytania'),
        ),
        migrations.AlterField(
            model_name='question',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_app.test', verbose_name='Test'),
        ),
        migrations.AlterField(
            model_name='test',
            name='test_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_category', to='test_app.category', verbose_name='Kategoria testu'),
        ),
        migrations.AlterField(
            model_name='test',
            name='test_creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_creator', to=settings.AUTH_USER_MODEL, verbose_name='Osoba tworząca test'),
        ),
        migrations.AlterField(
            model_name='test',
            name='test_duration',
            field=models.DurationField(default='00:00:00', help_text='Czas musi być zapisany w formacie HH:MM:SS', verbose_name='Czas trwania testu'),
        ),
        migrations.AlterField(
            model_name='test',
            name='test_end_login_time',
            field=models.TimeField(help_text='Czas musi być zapisany w formacie HH:MM:SS', verbose_name='Godzina zakończenia logowania do testu'),
        ),
        migrations.AlterField(
            model_name='test',
            name='test_opening_date',
            field=models.DateField(verbose_name='Dzień otwarcia testu'),
        ),
        migrations.AlterField(
            model_name='test',
            name='test_start_login_time',
            field=models.TimeField(help_text='Czas musi być zapisany w formacie HH:MM:SS', verbose_name='Godzina rozpoczęcia logowania do testu'),
        ),
        migrations.AlterField(
            model_name='test',
            name='test_title',
            field=models.CharField(max_length=100, unique=True, verbose_name='Nazwa testu'),
        ),
    ]
