# Generated by Django 4.2.6 on 2024-01-11 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration_app', '0006_alter_guardian_guardian_clause_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schoolteam',
            name='is_active',
            field=models.BooleanField(blank=True, default=False, verbose_name='is_active'),
        ),
    ]