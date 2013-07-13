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
