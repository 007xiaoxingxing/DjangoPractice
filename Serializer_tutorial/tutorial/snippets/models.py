# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from pygments.lexers import get_all_lexers
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
from pygments.styles import get_all_styles

import signals


LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([item[1][0], item[0]] for item in LEXERS)
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Snippet(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    owner = models.ForeignKey('auth.user', related_name='snippet', on_delete=models.CASCADE)
    highlighted = models.TextField()

    class Meta:
        ordering = ('created', )

    def save(self, *args, **kwargs):
        """
        把snippet使用pygments来生成高亮的html代码
        :param args:
        :param kwargs:
        :return:
        """
        lexer = get_lexer_by_name(self.language)
        linenos = self.linenos and 'table' or False
        options = self.title and {'title': self.title} or {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                  full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super(Snippet, self).save(*args, **kwargs)

        signals.snippet_saved.send(sender=self.__class__, obj=self, instance=self)


signals.snippet_saved.connect(receiver=signals.on_snippet_create, sender=Snippet)






