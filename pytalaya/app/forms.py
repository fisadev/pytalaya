#-*- coding:utf-8 -*-
from django import forms
from django.forms import ModelForm

from app.models import Team
from app.utils import get_or_none


class NewTeamForm(ModelForm):
    class Meta:
        model = Team

class JoinTeamForm(forms.Form):
    team_name = forms.CharField()
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(render_value=False))

    def clean(self):
        cleaned_data = super(JoinTeamForm, self).clean()
        team_name = cleaned_data.get('team_name')
        password = cleaned_data.get('password')

        team = get_or_none(Team, name=team_name)
        if team is None:
            raise forms.ValidationError("That team does not exists!")
        else:
            if password not in (team.admin_password, team.member_password):
                raise forms.ValidationError("Invalid password!")

        cleaned_data['team'] = team
        return cleaned_data

