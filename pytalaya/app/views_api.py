import json

from django.http import HttpResponse

from app.models import Team


def members(self, slug):
    team = Team.objects.get(slug=slug)
    return HttpResponse(json.dumps(team.members.select_related('area')),
                        content_type="application/json")
