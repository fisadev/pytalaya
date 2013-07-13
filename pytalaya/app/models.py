from django.db import models


class Team(models.Model):
    slug = models.SlugField(max_length=255)
    name = models.CharField(max_length=255)
    private = models.BooleanField()
    password = models.CharField(max_length=100)


class Group(models.Model):
    name = models.CharField(max_length=255)


class Member(models.Model):
    STATUS_OK = 'ok'
    STATUS_FREE = 'free'
    STATUS_WARNING = 'warning'
    STATUS_PROBLEM = 'problem'
    STATUSES = (
        (STATUS_OK, 'Ok'),
        (STATUS_FREE, 'Free'),
        (STATUS_WARNING, 'Warning'),
        (STATUS_PROBLEM, 'Problem'),
    )

    username = models.SlugField(max_length=255)
    team = models.ForeignKey(Team)
    group = models.ForeignKey(Group, null=True, blank=True)
    status = models.CharField(max_length=50, choices=STATUSES, default=STATUS_OK)
    status_info = models.TextField()
