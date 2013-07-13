from django.conf.urls import patterns, url
from app import views



urlpatterns = patterns('',
    url(r'^t/(?P<team_slug>[\w-]+)/$', 'app.views.dashboard', name='dashboard'),
    url(r'^join/(?P<team_slug>[\w-]+)?/?$', 'app.views.join', name='join'),
    url(r'^api/members/(?P<team_slug>[\w-]+)/$', 'app.views_api.members', name='api_members'),
    url(r'^api/status/(?P<member_id>\d+)/$', 'app.views_api.status', name='api_status'),
    url(r'^create/$', 'create', name='create'),
)
