#-*- coding:utf-8 -*-
from django.forms import ModelForm

from app.models import Team


class NewTeamForm(ModelForm):
    class Meta:
        model = Team
