#-*- coding:utf-8 -*-
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from forms import NewTeamForm, JoinTeamForm
from models import Team


def home(request):
    '''Home page.'''
    return render(request, 'home.html', {})

def contact(request):
    '''Contact page.'''
    return render(request, 'contact.html', {})

def new_team(request):
    '''Create new team.'''
    if request.method == 'POST':
        form = NewTeamForm(request.POST)
        if form.is_valid():
            team = form.save()
            request.session['team'] = team
            return HttpResponseRedirect(reverse(team_status))
    else:
        form = NewTeamForm()

    return render(request, 'new_team.html', {'form': form})

def join_team(request, team_url=None):
    '''Join an existing team.'''
    if request.method == 'POST':
        form = JoinTeamForm(request.POST)
        if form.is_valid():
            team = form.cleaned_data['team']
            request.session['team'] = team
            return HttpResponseRedirect(reverse(team_status, args=(team_url,)))
    else:
        form = JoinTeamForm()
        if team_url is not None:
            team = Team.objects.get(url=team_url)
            form.initial['team_name'] = team.name

    return render(request, 'join_team.html', {'form': form})

def team_status(request, team_url=None):
    '''View team status dashboard.'''
    team = request.session.get('team', None)
    if team is not None and (not team_url or team.url == team_url):
        return render(request, 'team_status.html', {'team': team})
    else:
        return HttpResponseRedirect(reverse(join_team, args=(team_url,)))

def my_status(request):
    '''Status reporting page.'''
    return None

