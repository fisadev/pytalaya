import json
import time
from datetime import datetime

from django.http import HttpResponse

from app.models import Member


def json_response(data):
    return HttpResponse(json.dumps(data),
                        content_type="application/json")


def members(request):
    team = request.session['member'].team
    members = team.members.select_related('area')

    return json_response(members)


def status(request, member_id):
    member = Member.objects.get(pk=member_id)

    if request.method == 'POST':
        member.status = request.POST.get('status', Member.STATUS_OK)
        member.status_info = request.POST.get('status_info', '')
        member.status_date = datetime.now()
        member.save()

    return json_response(member)


def events(request):
    team = request.session['member'].team

    def event_stream():
        last_update = datetime(1901, 1, 1)
        while True:
            changed_members = team.members.filter(status_date__gte=last_update)
            for member in changed_members:
                yield 'data: %s\n\n' % json.dumps(member)
            time.sleep(5)

    return HttpResponse(event_stream(), mimetype="text/event-stream")
