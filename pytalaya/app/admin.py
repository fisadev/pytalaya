#-*- coding:utf-8 -*-
from django.contrib import admin

from app.models import Team, Status, Member


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')
    search_fields = ('name', 'description')


class StatusAdmin(admin.ModelAdmin):
    list_display = ('team', 'name')
    list_filter = ('team', )
    search_fields = ('name', )


class MemberAdmin(admin.ModelAdmin):
    list_display = ('team', 'username', 'group_tags', 'status', 'status_date')
    list_filter = ('team', 'group_tags', 'status', 'status_date')
    search_fields = ('username', 'status', 'status_extra')
    date_hierarchy = 'status_date'


admin.site.register(Team, TeamAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Member, MemberAdmin)
