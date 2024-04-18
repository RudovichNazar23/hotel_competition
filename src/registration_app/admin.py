from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import HighSchool, Guardian, TeamMember, SchoolTeam


class HighSchoolAdmin(ModelAdmin):
    list_display = ("full_name", "city", "school_mobile_phone", "school_email")


class GuardianAdmin(ModelAdmin):
    list_display = ("guardian_name", "guardian_surname", "guardian_mobile_phone", "guardian_email")


class TeamMemberAdmin(ModelAdmin):
    list_display = ("member_name", "member_surname")


class SchoolTeamAdmin(ModelAdmin):
    list_display = ("high_school", "guardian", "first_member", "second_member", "is_active")
    list_filter = ("is_active",)


admin.site.register(HighSchool, HighSchoolAdmin)
admin.site.register(Guardian, GuardianAdmin)
admin.site.register(TeamMember, TeamMemberAdmin)
admin.site.register(SchoolTeam, SchoolTeamAdmin)
