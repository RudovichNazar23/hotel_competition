# Generated by Django 4.2.6 on 2023-12-11 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration_app', '0003_alter_guardian_guardian_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='highschool',
            name='short_name',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]