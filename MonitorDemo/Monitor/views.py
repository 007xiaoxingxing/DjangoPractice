# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import platform
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
        return Response("Windows")
        pass
    elif server_os == 'Linux':
        meminfo = OrderedDict()
        with open('/proc/meminfo') as f:
            for line in f:
                meminfo[line.split(':')[0]] = line.split(':')[1].strip()

        meminfo_model = MemoryInfo()
        meminfo_model.total = meminfo['MemTotal']
        meminfo_model.free = meminfo['MemFree']
        meminfo_model.available = meminfo['MemAvailable']
        meminfo_model.swap_free = meminfo['SwapFree']
        meminfo_model.cache = meminfo['Cached']
        meminfo_model.save()
        serializer = MemoryInfoSerializer(meminfo_model)
        content = JSONRenderer.render(serializer.data)
        return Response(content)



