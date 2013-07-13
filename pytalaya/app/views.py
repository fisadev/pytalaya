from .forms import JoinForm, TeamForm
from .models import Team, Member
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def dashboard(request, team_slug):
    '''
    Show dashbard of a team or redirect to join view.
    '''
    member = request.session.get('member')
    if member and team_slug == member.team.slug:
        return render(request,
                      'dashboard.html',
                      {'team': member.team, 'member': member})
    else:
        return HttpResponseRedirect(reverse('join', kwargs={'team_slug': team_slug}))


def create(request):
    '''
    Creates a new team.
    '''

    if request.method == "POST":
        form = TeamForm(request.POST)
        if form.is_valid():
            team = form.save()
            return HttpResponseRedirect(reverse('join', kwargs={'team_slug': team.slug}))
    else:
        form = TeamForm()
    return render(request, 'create.html', {'form': form})


def join(request, team_slug=None):
    '''
    Join to team and redirect to dashboard of the team.
    '''

    if request.method == 'POST':
        form = JoinForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['user_name']
            team_slug = form.cleaned_data['team']
            team = Team.objects.get(slug=team_slug)
            user = Member(username=user_name, team=team)
            user.save()
            request.session['member'] = user
            return HttpResponseRedirect(reverse('dashboard', kwargs={'team_slug': team_slug}))
    else:
        form = JoinForm()
        form.fields['team'].initial = team_slug
    return render(request, 'join.html', {'form': form})
