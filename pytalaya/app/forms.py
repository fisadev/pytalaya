#-*- coding:utf-8 -*-
from django import forms
from django.forms import ModelForm

from app.models import Team


class NewTeamForm(ModelForm):
    class Meta:
        model = Team

class JoinTeamForm(forms.Form):
    team_name = forms.CharField()
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(render_value=False))
