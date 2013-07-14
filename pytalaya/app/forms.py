# coding: utf-8
from django import forms

from app.models import Team, Member


class TeamForm(forms.Form):
    slug = forms.SlugField(max_length=255)
    name = forms.CharField(max_length=255)
    private = forms.BooleanField(required=False)
    password = forms.CharField(required=False,max_length=100)
    area_name = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows':6, 'cols':100}))


class JoinForm(forms.Form):
    user_name = forms.CharField(max_length=100)
    team = forms.SlugField(max_length=255)
    password = forms.CharField(required=False, max_length=100)

    def clean_team(self):
        #team must exists
        team = self.cleaned_data['team']
        if not Team.objects.filter(slug=team).exists():
            raise forms.ValidationError('Team must exists')
        return team

    def clean(self):
        cleaned_data = super(JoinForm, self).clean()
        password = cleaned_data.get("password")
        team = cleaned_data.get("team")
        user = self.cleaned_data.get("user_name")

        team = Team.objects.get(slug=team)

        #user must not exists in this team
        if Member.objects.filter(username=user, team=team).exists():
            raise forms.ValidationError('User already exists in this team. Choose another username.')

        if team.private and team.password != password:
            msg = "Incorrect password."
            self._errors["password"] = self.error_class([msg])
            del cleaned_data["password"]

        return cleaned_data

