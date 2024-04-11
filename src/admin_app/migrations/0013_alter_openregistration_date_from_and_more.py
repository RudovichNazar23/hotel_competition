# Generated by Django 4.2.6 on 2024-04-11 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0012_alter_openregistration_date_from_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='openregistration',
            name='date_from',
            field=models.DateField(default=11, verbose_name='Dzień rozpoczęcia rejestracji'),
        ),
        migrations.AlterField(
            model_name='openregistration',
            name='date_to',
            field=models.DateField(default=11, verbose_name='Dzień zakończenia rejestracji'),
        ),
    ]
