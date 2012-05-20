#-*- coding:utf-8 -*-
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from app.forms import NewTeamForm, JoinTeamForm
from app.models import Team


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
            return HttpResponseRedirect(reverse(join_team, args=(team.url,)))
    else:
        form = NewTeamForm()

    return render(request, 'new_team.html', {'form': form})

def join_team(request, team_url=None):
    '''Join an existing team.'''
    if request.method == 'POST':
        form = JoinTeamForm(request.POST)
        if form.is_valid():
            team = form.cleaned_data['team']
            password = form.cleaned_data['password']
            request.session['team'] = team
            if password == team.admin_password:
                return HttpResponseRedirect(reverse(team_status))
            elif password == team.member_password:
                return HttpResponseRedirect(reverse(my_status))
    else:
        form = JoinTeamForm()
        if team_url is not None:
            team = Team.objects.get(url=team_url)
            form.initial['team_name'] = team.name

    return render(request, 'join_team.html', {'form': form})

def team_status(request):
    '''View team status dashboard.'''
    team = request.session.get('team', None)
    if team is None:
        return HttpResponseRedirect(reverse(join_team))
    else:
        return render(request, 'team_status.html', {})

def my_status(request):
    '''Status reporting page.'''
    return None

def leave(request):
    '''Leave current team.'''
    request.session['team'] = None
    return HttpResponseRedirect(reverse(home))

