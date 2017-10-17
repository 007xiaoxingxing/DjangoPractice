# -*- coding:utf-8 -*-
from models import CapacityRatio
from rest_framework import serializers


class CapacityRatioLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = CapacityRatio
        fields = ('stat_time', 'customer_buy', 'system_total')