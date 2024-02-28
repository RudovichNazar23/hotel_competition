# Generated by Django 4.2.6 on 2024-02-28 17:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('registration_app', '0009_alter_guardian_options_alter_highschool_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_content', models.TextField(max_length=100, verbose_name='Treść odpowiedzi')),
            ],
            options={
                'verbose_name_plural': 'Odpowiedzi',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_title', models.CharField(max_length=100, unique=True, verbose_name='Nazwa kategorii')),
                ('category_description', models.TextField(blank=True, max_length=200, verbose_name='Opis kategorii')),
            ],
            options={
                'verbose_name_plural': 'Kategorie',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_content', models.TextField(max_length=100, verbose_name='Treść pytania')),
                ('question_attachment', models.FileField(blank=True, upload_to='question_attachments/', verbose_name='Załącznik dla pytania')),
                ('question_correct_answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='correct_answer', to='test_app.answer', verbose_name='Poprawna odpowiedz')),
                ('question_incorrect_answers', models.ManyToManyField(related_name='incorrect_answers', to='test_app.answer', verbose_name='Niepoprawne odpowiedzi')),
            ],
            options={
                'verbose_name_plural': 'Pytania',
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_title', models.CharField(max_length=100, unique=True, verbose_name='Nazwa testu')),
                ('test_passing_time', models.TimeField(verbose_name='Czas wykonywania testu')),
                ('test_date', models.DateField(unique=True, verbose_name='Data otwarcia testu')),
                ('test_start_login_time', models.TimeField(verbose_name='Czas otwarcia logowania')),
                ('test_end_login_time', models.TimeField(verbose_name='Czas zamknięcia logowania')),
                ('test_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_category', to='test_app.category', verbose_name='Kategoria testu')),
                ('test_creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_creator', to=settings.AUTH_USER_MODEL)),
                ('test_questions', models.ManyToManyField(related_name='test_questions', to='test_app.question')),
            ],
            options={
                'verbose_name_plural': 'Testy',
            },
        ),
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('competition_test_result', models.CharField(max_length=100)),
                ('competition_test_performer_pass_time', models.TimeField()),
                ('competition_test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_app.test')),
                ('competition_test_performer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration_app.teammember')),
            ],
        ),
    ]
