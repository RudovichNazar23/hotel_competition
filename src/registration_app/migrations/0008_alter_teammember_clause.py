# Generated by Django 4.2.6 on 2023-11-05 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration_app', '0007_alter_guardian_clause_alter_guardian_guardian_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammember',
            name='clause',
            field=models.FileField(blank=True, upload_to='clauses/'),
        ),
    ]