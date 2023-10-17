from django.contrib import admin
from .models import HighSchool, Guardian, TeamMember, SchoolTeam

admin.site.register(HighSchool)
admin.site.register(Guardian)
admin.site.register(TeamMember)
admin.site.register(SchoolTeam)
