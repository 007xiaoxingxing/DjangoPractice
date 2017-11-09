# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CapacityRatio(models.Model):
    id = models.AutoField(primary_key=True)
    stat_time = models.DateTimeField(auto_now=True, null=False)
    customer_buy = models.BigIntegerField()
    system_total = models.BigIntegerField()
