# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import time
from django.db import models

OS_TYPE = (
    ('L', 'Linux'),
    ('W', 'Windows')
)

SERVER_USE_TYPE = (
    ('Web', 'Web Server'),
    ('Dev', 'Dev Server'),
    ('DB', 'DB Server')
)


class Server(models.Model):
    """
    服务器model，包含服务器基本信息，ip，所属部门，创建时间，是否在用,服务器类型
    """
    ip = models.CharField(max_length=32)
    server_name = models.CharField(max_length=100)
    os_type = models.CharField(max_length=20, choices=OS_TYPE, default='L')
    created = models.DateTimeField(auto_now_add=True)
    department = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    server_use_type = models.CharField(max_length=100, choices=SERVER_USE_TYPE, default='Web')


class MemoryInfo(models.Model):
    """
    服务器内存状态信息，总内存，使用内存，共享内存，缓冲内存，可用内存和swap大小,获取时间
    """
    server = models.ForeignKey(Server, on_delete=models.CASCADE, null=True)
    total = models.BigIntegerField()
    free = models.BigIntegerField()
    cache = models.BigIntegerField()
    available = models.BigIntegerField()
    shared = models.BigIntegerField()
    update_time = models.DateTimeField(auto_now_add=True)


class CPUInfo(models.Model):
    """
    服务器当前CPU信息
    """
    user = models.BigIntegerField()
    idle = models.BigIntegerField()


class NetInfo(models.Model):
    """
    服务器网络信息
    """

    port_list = models.TextField()
    in_speed = models.BigIntegerField()
    up_speed = models.BigIntegerField()


class OnlineUserInfo(models.Model):
    """
    服务器当前登录的用户信息
    """
    login_user_number = models.IntegerField()
    login_user_name_list = models.TextField()











