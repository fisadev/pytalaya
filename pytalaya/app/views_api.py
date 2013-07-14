# coding: utf-8
import json
import time
from datetime import datetime

from django.http import HttpResponse
from django.core.serializers import serialize

from app.models import Member


def json_response(data, orm_objects=True):
    if orm_objects:
        json_data = serialize('json', data)
    else:
        json_data = json.dumps(data)
    return HttpResponse(json_data,
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
            last_update = datetime.now()

            for member in changed_members:
                yield 'data: %s\n\n' % serialize('json', [member, ])

            time.sleep(5)

    return HttpResponse(event_stream(), mimetype="text/event-stream")
