from django.contrib.auth.models import User
from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    ingredients = models.TextField(blank=True, null=True)
    directions = models.TextField(blank=True, null=True)

    link = models.URLField(blank=True, null=True)

    time_created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title


class Ribbon(models.Model):
    recipe = models.ForeignKey(Recipe)
    user = models.ForeignKey(User)
    comments = models.TextField(blank=True, null=True)
    time_created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '{0} Ribbon for {1}'.format(unicode(self.recipe),
                                           unicode(self.user))

class Tag(models.Model):
    ribbon = models.ForeignKey(Ribbon)
    key = models.CharField(max_length=50)
    originalKey = models.CharField(max_length=50)
    value = models.CharField(max_length=50, blank=True, null=True)
    originalValue = models.CharField(max_length=50, blank=True, null=True)

    def __unicode__(self):
        return '{0}: {1}'.format(self.originalKey, self.originalValue)
    
