import json

from django.http import HttpResponse

from app.models import Team


def members(self, slug):
    team = Team.objects.get(slug=slug)
    return HttpResponse(json.dumps(team.members.all()),
                        content_type="application/json")
