# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import AwardsAndAchievements, Projects, Notes,\
    Summary, Experience, Contact

admin.site.register(Projects)
admin.site.register(Notes)
admin.site.register(Experience)
admin.site.register(Summary)
admin.site.register(AwardsAndAchievements)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'subject', 'message_date')
    ordering = ('-message_date',)

admin.site.register(Contact, ContactAdmin)

admin.site.site_header = "Rahul Kumeriya's Portfolio"
admin.site.unregister(Group)
admin.site.unregister(User)
