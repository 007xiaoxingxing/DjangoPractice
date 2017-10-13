# -*- coding:utf-8 -*-
from django.conf.urls import url
from django.conf.urls import include
from rest_framework.urlpatterns import format_suffix_patterns
from Monitor import views


urlpatterns = format_suffix_patterns(
    [
        url(r'^servers/$',
            views.ServerList.as_view(),
            name='server-list'),
        url(r'^servers/(?P<pk>[0-9]+)/$',
            views.ServerDetail.as_view(),
            name='server-detail'),
        url(r'^meminfo/$', views.server_meminfo)
    ]
)