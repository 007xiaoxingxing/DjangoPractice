# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import platform
import psutil
from collections import OrderedDict

from django.shortcuts import render
from Monitor.serializers import ServerSerializer
from Monitor.models import Server
from Monitor.models import MemoryInfo
from Monitor.serializers import MemoryInfoSerializer
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer


class ServerList(generics.ListCreateAPIView):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer


class ServerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer


@api_view(['GET'])
def server_meminfo(request, format=None):
    server_os = platform.system()
    if server_os == 'Windows':
        server = Server.objects.get(pk=1)
        mem = psutil.virtual_memory()
        meminfo_model = MemoryInfo(total=mem.total, free=mem.free,
                                   cache=0L, available=mem.available,
                                   shared=0L)
        meminfo_model.server = server
        meminfo_serializer = MemoryInfoSerializer(meminfo_model)
        meminfo_model.save()
        return Response(meminfo_serializer.data)
    elif server_os == 'Linux':
        server = Server.objects.get(pk=2)
        mem = psutil.virtual_memory()
        meminfo_model = MemoryInfo(total=mem.total, free=mem.free,
                                   cache=mem.cached, available=mem.available,
                                   shared=mem.shared)
        meminfo_model.server = server
        meminfo_serializer = MemoryInfoSerializer(meminfo_model)
        meminfo_model.save()
        return Response(meminfo_serializer.data)



