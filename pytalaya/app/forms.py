# -*- coding: utf-8 -*-
from django import forms
from app.models import Team, Member


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team


class JoinForm(forms.Form):
    user_name = forms.CharField(max_length=100)
    team = forms.SlugField(max_length=255)

    def clean_user_name(self):
        #user must not exists
        user = self.cleaned_data['user_name']
        if Member.objects.filter(username=user).exists():
            raise forms.ValidationError('User already exists. Choose another.')
        return user

    def clean_team(self):
        #team must exists
        team = self.cleaned_data['team']
        if not Team.objects.filter(slug=team).exists():
            raise forms.ValidationError('Team must exists')
        return team
