# Generated by Django 4.2.6 on 2023-12-11 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='schoolteam',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]