# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from rest_framework import viewsets
from quickstart.serializers import UserSerializer, GroupSerializer

from django.shortcuts import render

class UserViewSet(viewsets.ModelViewSet):
    """
    API端：允许查看和编辑用户
    """

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API端：允许查看和编辑用户组
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
