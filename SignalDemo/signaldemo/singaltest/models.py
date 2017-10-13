# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models



class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)



