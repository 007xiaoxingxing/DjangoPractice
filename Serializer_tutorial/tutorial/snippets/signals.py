# -*- coding:utf-8 -*-
from django.db.models.signals import post_save
from django.dispatch import receiver
#from snippets.models import Snippet
import django.dispatch
import logging

snippet_saved = django.dispatch.Signal(providing_args=['obj'])

#@receiver(post_save, sender=Snippet)
def on_snippet_create(sender,instance, **kwargs):
    logging.debug("New Snippet")
    print "New snippet created!"
    print "The code = %s" % instance.code







