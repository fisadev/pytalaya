from django.conf.urls import patterns, include, url
from pytalaya import views


urlpatterns = patterns('',
    url(r'^t/(?P<slug>[\w-]+)/$', views.dashboard),
    url(r'^api/members/(?P<team_slug>[\w-]+)/$', 'app.views_api.members', name='api_members'),
    url(r'^api/status/(?P<member_id>\d+)/$', 'app.views_api.status', name='api_status'),
)
