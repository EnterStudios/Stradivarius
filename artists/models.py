from django.db import models
#from django.db.models import Q
from django.conf import settings
from djangoyearlessdate.models import YearField


#incorparate a custom model manager like the following to create a
#special search filter...
# usage: Musicians.search(filter...)
class MusicianManager(models.Manager):
    def search(self, term):
        pass

class Musician(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    instrument = models.CharField('instrument', max_length = 254, null=False, blank=True)

    objects = MusicianManager()

    #ordering for search results...
    class Meta:
        ordering = ["instrument"]

    def __unicode__(self):
        return u'%s -- %s' % (self.user.username, self.instrument)

