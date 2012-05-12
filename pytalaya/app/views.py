#-*- coding:utf-8 -*-
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from forms import NewTeamForm
from models import Team


def home(request):
    '''Home page.'''
    return render(request, 'home.html', {})

def contact(request):
    '''Contact page.'''
    return render(request, 'contact.html', {})

@login_required
def account(request):
    '''Account settings page.'''
    return render(request, 'account.html', {})

def new_team(request):
    '''Create new team.'''
    if request.method == 'POST':
        form = NewTeamForm(request.POST)
        if form.is_valid():
            team = form.save()
    else:
        form = NewTeamForm()

    return render(request, 'new_team.html', {'form': form})

def join_team(request):
    '''Join an existing team.'''
    return None

def team_status(request):
    '''View team status dashboard.'''
    return None

def team_settings(request):
    '''Edit team settings.'''
    return None

def my_status(request):
    '''Status reporting page.'''
    return None

