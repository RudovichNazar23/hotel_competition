# Generated by Django 4.2.6 on 2024-03-25 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0007_alter_answer_options_alter_question_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_attachment',
            field=models.FileField(blank=True, upload_to='question_attachments/', verbose_name='Załącznik dla pytania'),
        ),
    ]