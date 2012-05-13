#-*- coding:utf-8 -*-
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from forms import NewTeamForm
from models import Team


def home(request):
    '''Home page.'''
    return render(request, 'home.html', {})

def contact(request):
    '''Contact page.'''
    return render(request, 'contact.html', {})

def new(request):
    '''Create new team.'''
    if request.method == 'POST':
        form = NewTeamForm(request.POST)
        if form.is_valid():
            new_team = form.save()
            return HttpResponseRedirect(reverse(team))
    else:
        form = NewTeamForm()

    return render(request, 'new.html', {'form': form})

def join(request, team=None):
    '''Join an existing team.'''
    return render(request, 'join.html', {})

def team(request):
    '''View team status dashboard.'''
    return render(request, 'team.html', {})

def me(request):
    '''Status reporting page.'''
    return None

