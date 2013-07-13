from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse


def dashboard(request, slug):
    '''
    Show dashbard of a team or redirect to join view.
    '''
    member = request.session.get('member')
    if member and slug == member.team.slug:
        pass
        #return HttpResponse()
    else:
        return HttpResponseRedirect(reverse('join', kwargs={'team_slug': slug}))