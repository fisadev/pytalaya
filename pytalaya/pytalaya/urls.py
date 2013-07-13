from django.conf.urls import patterns, url

urlpatterns = patterns('app.views',
    url(r'^home/$', 'home', name='home'),
    url(r'^t/(?P<team_slug>[\w-]+)/$', 'dashboard', name='dashboard'),
    url(r'^join/(?P<team_slug>[\w-]+)?/?$', 'join', name='join'),
    url(r'^create/$', 'create', name='create'),
)

urlpatterns += patterns('app.views_api',
    url(r'^api/members/(?P<team_slug>[\w-]+)/$', 'members', name='api_members'),
    url(r'^api/status/(?P<member_id>\d+)/$', 'status', name='api_status'),
)
