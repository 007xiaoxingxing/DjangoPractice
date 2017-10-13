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
        url(r'^memnow/$',
            views.server_meminfo,
            ),
        url(r'^meminfo/$',
            views.MemoryInfoDetail.as_view(),
            name='server-meminfo-list'
            ),
        url(r'^meminfo/(?P<server_id>[0-9]+)/(?P<seconds>[0-9]+)/$',
            views.MemoryInfoDetail.as_view(),
            name='server-meminfo-filter'
            )
    ]
)