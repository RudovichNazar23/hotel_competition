# Generated by Django 4.2.6 on 2024-04-10 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration_app', '0009_alter_guardian_options_alter_highschool_options_and_more'),
        ('test_app', '0012_teammembertestsession_team_member_client'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='teammembertestsession',
            unique_together={('team_member', 'member_uidb64', 'team_member_client')},
        ),
    ]
