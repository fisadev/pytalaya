#-*- coding:utf-8 -*-
from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

# normal views
urlpatterns = patterns('app.views',
    url(r'^$', 'home', name='home'),

    url(r'^new_team/$', 'new_team', name='new_team'),
    url(r'^join_team/$', 'join_team', name='join_team'),

    url(r'^team_status/$', 'team_status', name='team_status'),
    url(r'^team_settings/$', 'team_settings', name='team_settings'),
    url(r'^my_status/$', 'my_status', name='my_status'),
)

# ajax views
urlpatterns += patterns('app.ajax_views',
    url(r'^ajax/get_status/$', 'get_status', name='get_status'),
    url(r'^ajax/report_status/$', 'report_status', name='report_status'),

    url(r'^ajax/add_group_tag/$', 'add_group_tag', name='add_group_tag'),
    url(r'^ajax/remove_group_tag/$', 'remove_group_tag', name='remove_group_tag'),

    url(r'^ajax/delete_member/$', 'delete_member', name='delete_member'),
)

# other apps urls
urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
)
