import json

from django.http import HttpResponse

from app.models import Team, Member


def json_response(data):
    return HttpResponse(json.dumps(data),
                        content_type="application/json")


def members(request, team_slug):
    team = Team.objects.get(slug=team_slug)
    members = team.members.select_related('area')

    return json_response(members)


def status(request, member_id):
    member = Member.objects.get(pk=member_id)

    if request.method == 'POST':
        member.status = request.POST.get('status', Member.STATUS_OK)
        member.status_info = request.POST.get('status_info', '')
        member.save()

    return json_response(member)
