import json

from django.http import HttpResponse

from app.models import Team


def members(self, team_slug):
    team = Team.objects.get(slug=team_slug)
    members = team.members.select_related('area')

    return HttpResponse(json.dumps(members),
                        content_type="application/json")
