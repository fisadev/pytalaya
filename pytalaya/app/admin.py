#-*- coding:utf-8 -*-
from django.contrib import admin
from models import Team, Status, Member, User


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'private', 'require_auth')
    list_filter = ('private', 'require_auth')
    search_fields = ('name', 'description')


class StatusAdmin(admin.ModelAdmin):
    list_display = ('team', 'name')
    list_filter = ('team', )
    search_fields = ('name', )


class MemberAdmin(admin.ModelAdmin):
    list_display = ('team', 'role', 'group_tags', 'user', 'status', 'status_date')
    list_filter = ('team', 'role', 'group_tags', 'status', 'status_date')
    search_fields = ('user__name', 'status', 'status_extra')
    date_hierarchy = 'status_date'


class UserAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', )


admin.site.register(Team, TeamAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(User, UserAdmin)
