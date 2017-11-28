# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)


class Tag(models.Model):
    name = models.CharField(max_length=100)


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField()
    create_time = models.DateTimeField(auto_now=True)


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=120)
    content = models.TextField()
    create_time = models.DateTimeField(auto_now=True)
    update_time = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category)
    tag = models.ManyToManyField(Tag)
    author = models.ForeignKey(User)