from django.conf.urls import patterns, include, url
from pytalaya import views


urlpatterns = patterns('',
    url(r'^t/(?P<slug>[\w-]+)/$', views.dashboard),
    url(r'^api/members/(?P<slug>[\w-]+)/$', 'pytalaya.views_api.members', name='api_members'),
)
