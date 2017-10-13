# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class SnippetsConfig(AppConfig):
    name = 'snippets'

    def ready(self):
        # import signal handlers
        import snippets.signals
