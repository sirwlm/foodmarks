from django.contrib.auth.models import User
from django.db import models

from foodmarks.fm.constants import *

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField(blank=True, null=True, max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    ingredients = models.TextField(blank=True, null=True)
    directions = models.TextField(blank=True, null=True)

    time_created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.link == '':
            self.link = None
        super(Recipe, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-time_created']


class Ribbon(models.Model):
    recipe = models.ForeignKey(Recipe)
    user = models.ForeignKey(User)
    comments = models.TextField(blank=True, null=True,
                                verbose_name="my comments")
    time_created = models.DateTimeField(auto_now_add=True)

    is_boxed = models.BooleanField(default=False)
    is_used = models.BooleanField(default=False)
    thumb = models.NullBooleanField(blank=True, null=True)

    def __unicode__(self):
        return u'{0} Ribbon for {1}'.format(unicode(self.recipe),
                                           unicode(self.user))

    class Meta:
        unique_together = ('recipe', 'user',)
        ordering = ['-time_created']

class Tag(models.Model):
    ribbon = models.ForeignKey(Ribbon)
    key = models.CharField(max_length=50)
    value = models.CharField(max_length=50, blank=True, null=True)

    def __unicode__(self):
        return u'{0}: {1}'.format(self.key, self.value)
