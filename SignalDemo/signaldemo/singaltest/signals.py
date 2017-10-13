from django.dispatch import Signal
from singaltest.models import Article


on_article_save = Signal(providing_args=['obj'])


def on_article_saved(sender, **kwargs):
    print "Article saved!"
    print "Article title = %s" % sender.title


on_article_save.connect(on_article_save, sender=Article)


