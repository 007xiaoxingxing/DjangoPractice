# -*- coding:utf-8 -*-
from Monitor.models import Server
from Monitor.models import MemoryInfo
from Monitor.models import MemoryInfo
from Monitor.models import CPUInfo
from Monitor.models import NetInfo
from Monitor.models import OnlineUserInfo
from rest_framework import serializers


class ServerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Server
        fields = ('id', 'ip', 'server_name',
                  'created', 'department', 'status',
                  'server_type')

    def create(self, validated_data):
        return Server.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.ip = validated_data.get('ip', instance.ip)
        instance.server_name = validated_data.get('server_name', instance.server_name)
        instance.created = validated_data.get('created', instance.created)
        instance.department = validated_data.get('department', instance.department)
        instance.status = validated_data.get('status', instance.status)
        instance.server_type = validated_data.get('server_type', instance.server_type)
        instance.save()
        return instance


class MemoryInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MemoryInfo
        fields = ('id', 'total', 'free', 'cache', 'swap_free', 'available')

    def create(self, validated_data):
        return MemoryInfo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.total = validated_data.get('total', instance.total)
        instance.free = validated_data.get('free', instance.free)
        instance.cache = validated_data.get('cache', instance.cache)
        instance.swap_free = validated_data.get('swap_free', instance.swap_free)
        instance.available = validated_data.get('available', instance.available)
        instance.save()
        return instance
