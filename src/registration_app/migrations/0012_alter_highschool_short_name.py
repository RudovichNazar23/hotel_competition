# Generated by Django 4.2.6 on 2023-11-07 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration_app', '0011_alter_highschool_full_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='highschool',
            name='short_name',
            field=models.CharField(max_length=255),
        ),
    ]
