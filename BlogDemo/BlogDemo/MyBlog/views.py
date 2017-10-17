# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets
from models import CapacityRatio
from serializers import CapacityRatioLogSerializer
# Create your views here.
class CapacityRatioLogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CapacityRatio.objects.all()
    serializer_class = CapacityRatioLogSerializer
