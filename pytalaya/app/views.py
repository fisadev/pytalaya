#-*- coding:utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response

from forms import NewTeamForm
from models import Team

def home(request):
    '''Home page.'''
    return render_to_response('home.html',
                              {},
                              context_instance=RequestContext(request))

def new_team(request):
    '''Create new team.'''
    if request.method == 'POST':
        form = NewTeamForm(request.POST)
        if form.is_valid():
            team = form.save()
    else:
        form = NewTeamForm()

    return render_to_response('new_team.html',
                              {'form': form},
                              context_instance=RequestContext(request))

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

