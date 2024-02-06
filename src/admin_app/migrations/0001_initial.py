# Generated by Django 4.2.6 on 2024-01-31 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OpenRegistrationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Data')),
                ('time_from', models.TimeField(verbose_name='Czas pozpoczęcia rejestracji')),
                ('time_to', models.TimeField(verbose_name='Czas zakończenia rejestracji')),
            ],
        ),
    ]