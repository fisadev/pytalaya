#-*- coding:utf-8 -*-
from django.db import models


class Team(models.Model):
    '''Team of people.'''
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    logo = models.ImageField(upload_to='logos')
    url = models.CharField(max_length=15, unique=True)

    admin_password = models.CharField(max_length=100, blank=True)
    member_password = models.CharField(max_length=100, blank=True)

    def __unicode__(self):
        return self.name


class Status(models.Model):
    '''Possible status of a team member.'''
    team = models.ForeignKey(Team)

    name = models.CharField(max_length=100)
    color = models.CharField(max_length=25)


class Member(models.Model):
    '''A team member.'''
    team = models.ForeignKey(Team)
    username = models.CharField(max_length=100)

    group_tags = models.TextField()

    status = models.ForeignKey(Status)
    status_extra = models.TextField()
    status_date = models.DateTimeField(auto_now=True)

