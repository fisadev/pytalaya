from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response

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


def create(request):
    '''Creates a new team'''
    
    if request.method == "POST":
	form = TeamForm(request.POST)
	if form.is_valid():
	    team = form.save()
	HttpResponseRedirect('/join')
    else:
        form = TeamForm()

    ctx = {'form':form}
    return render_to_response('', ctx, context_instance=RequestContext(request))



