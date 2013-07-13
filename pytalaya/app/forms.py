# -*- coding: utf-8 -*-
from django import forms
from pytalaya.models import Team

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = '__all__'

class JoinForm(forms.Form):
    user_name = forms.CharField(max_length=100)
    team = forms.SlugField(max_length=255)

