from django.contrib.auth.models import User
from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    ingredients = models.TextField(blank=True, null=True)
    directions = models.TextField(blank=True, null=True)

    link = models.URLField(blank=True, null=True)

    time_created = models.DateTimeField(auto_now_add=True)

class Tag(models.Model):
    recipe = models.ForeignKey(Recipe)
    user = models.ForeignKey(User)
    key = models.CharField(max_length=50)
    value = models.CharField(max_length=50)
