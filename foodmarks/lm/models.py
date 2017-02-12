import datetime

from django.contrib.auth.models import User
from django.db import models

from constants import *


class LiquidFlavors(models.Model):
    flvid = models.CharField(primary_key=True, max_length=12)
    name = models.CharField(max_length=60)
    flvm = models.CharField(max_length=40)
    murl = models.URLField(blank=True, null=True, max_length=255, unique=True)
    flvurl = models.URLField(blank=True, null=True, max_length=255, unique=True)
    flvnotes = models.CharField(max_length=-1, blank=True, null=True)
    rating = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)



class LiquidRecipes(models.Model):
    ufid = models.CharField(primary_key=True, max_length=12)
    recipename = models.CharField(max_length=40)
    recipeauthor = models.ForeignKey(User)
    rating = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    flv1 = models.ForeignKey(LiquidFlavors, models.DO_NOTHING, db_column='flv1', blank=True, null=True, related_name="flavor_name1")
    flvm1 = models.ForeignKey(LiquidFlavors, models.DO_NOTHING, db_column='flvm1', blank=True, null=True, related_name="flvm1")
    flvp1 = models.DecimalField(max_digits=4, decimal_places=4, blank=True, null=True)
    flv2 = models.ForeignKey(LiquidFlavors, models.DO_NOTHING, db_column='flv2', blank=True, null=True, related_name="flavor_name2")
    flvm2 = models.ForeignKey(LiquidFlavors, models.DO_NOTHING, db_column='flvm2', blank=True, null=True, related_name="flvm2")
    flvp2 = models.DecimalField(max_digits=4, decimal_places=4, blank=True, null=True)
    flv3 = models.ForeignKey(LiquidFlavors, models.DO_NOTHING, db_column='flv3', blank=True, null=True, related_name="flavor_name3")
    flvm3 = models.ForeignKey(LiquidFlavors, models.DO_NOTHING, db_column='flvm3', blank=True, null=True, related_name="flvm3")
    flvp3 = models.DecimalField(max_digits=4, decimal_places=4, blank=True, null=True)
    flv4 = models.ForeignKey(LiquidFlavors, models.DO_NOTHING, db_column='flv4', blank=True, null=True, related_name="flavor_name4")
    flvm4 = models.ForeignKey(LiquidFlavors, models.DO_NOTHING, db_column='flvm4', blank=True, null=True, related_name="flvm4")
    flvp4 = models.DecimalField(max_digits=4, decimal_places=4, blank=True, null=True)
    flv5 = models.ForeignKey(LiquidFlavors, models.DO_NOTHING, db_column='flv5', blank=True, null=True, related_name="flavor_name5")
    flvm5 = models.ForeignKey(LiquidFlavors, models.DO_NOTHING, db_column='flvm5', blank=True, null=True, related_name="flvm5")
    flvp5 = models.DecimalField(max_digits=4, decimal_places=4, blank=True, null=True)
    flv6 = models.ForeignKey(LiquidFlavors, models.DO_NOTHING, db_column='flv6', blank=True, null=True, related_name="flavor_name6")
    flvm6 = models.ForeignKey(LiquidFlavors, models.DO_NOTHING, db_column='flvm6', blank=True, null=True, related_name="flvm6")
    flvp6 = models.DecimalField(max_digits=4, decimal_places=4, blank=True, null=True)
    flv7 = models.ForeignKey(LiquidFlavors, models.DO_NOTHING, db_column='flv7', blank=True, null=True, related_name="flavor_name7")
    flvm7 = models.ForeignKey(LiquidFlavors, models.DO_NOTHING, db_column='flvm7', blank=True, null=True, related_name="flvm7")
    flvp7 = models.DecimalField(max_digits=4, decimal_places=4, blank=True, null=True)
    flv8 = models.ForeignKey(LiquidFlavors, models.DO_NOTHING, db_column='flv8', blank=True, null=True, related_name="flavor_name8")
    flvm8 = models.ForeignKey(LiquidFlavors, models.DO_NOTHING, db_column='flvm8', blank=True, null=True, related_name="flvm8")
    flvp8 = models.DecimalField(max_digits=4, decimal_places=4, blank=True, null=True)
    flv9 = models.ForeignKey(LiquidFlavors, models.DO_NOTHING, db_column='flv9', blank=True, null=True, related_name="flavor_name9")
    flvm9 = models.ForeignKey(LiquidFlavors, models.DO_NOTHING, db_column='flvm9', blank=True, null=True, related_name="flvm9")
    flvp9 = models.DecimalField(max_digits=4, decimal_places=4, blank=True, null=True)
    flv10 = models.ForeignKey(LiquidFlavors, models.DO_NOTHING, db_column='flv10', blank=True, null=True, related_name="flavor_name10")
    flvm10 = models.ForeignKey(LiquidFlavors, models.DO_NOTHING, db_column='flvm10', blank=True, null=True, related_name="flvm10")
    flvp10 = models.DecimalField(max_digits=4, decimal_places=4, blank=True, null=True)
    flv11 = models.ForeignKey(LiquidFlavors, models.DO_NOTHING, db_column='flv11', blank=True, null=True, related_name="flavor_name11")
    flvm11 = models.ForeignKey(LiquidFlavors, models.DO_NOTHING, db_column='flvm11', blank=True, null=True, related_name="flvm11")
    flvp11 = models.DecimalField(max_digits=4, decimal_places=4, blank=True, null=True)
    flv12 = models.ForeignKey(LiquidFlavors, models.DO_NOTHING, db_column='flv12', blank=True, null=True, related_name="flavor_name12")
    flvm12 = models.ForeignKey(LiquidFlavors, models.DO_NOTHING, db_column='flvm12', blank=True, null=True, related_name="flvm12")
    flvp12 = models.DecimalField(max_digits=4, decimal_places=4, blank=True, null=True)
    flv13 = models.ForeignKey(LiquidFlavors, models.DO_NOTHING, db_column='flv13', blank=True, null=True, related_name="flavor_name13")
    flvm13 = models.ForeignKey(LiquidFlavors, models.DO_NOTHING, db_column='flvm13', blank=True, null=True, related_name="flvm13")
    flvp13 = models.DecimalField(max_digits=4, decimal_places=4, blank=True, null=True)
    flv14 = models.ForeignKey(LiquidFlavors, models.DO_NOTHING, db_column='flv14', blank=True, null=True, related_name="flavor_name14")
    flvm14 = models.ForeignKey(LiquidFlavors, models.DO_NOTHING, db_column='flvm14', blank=True, null=True, related_name="flvm14")
    flvp14 = models.DecimalField(max_digits=4, decimal_places=4, blank=True, null=True)
    flv15 = models.ForeignKey(LiquidFlavors, models.DO_NOTHING, db_column='flv15', blank=True, null=True, related_name="flavor_name15")
    flvm15 = models.ForeignKey(LiquidFlavors, models.DO_NOTHING, db_column='flvm15', blank=True, null=True, related_name="flvm15")
    flvp15 = models.DecimalField(max_digits=4, decimal_places=4, blank=True, null=True)
    glycerinratio = models.CharField(max_length=5, blank=True, null=True)
    flavtotalp = models.DecimalField(max_digits=4, decimal_places=4, blank=True, null=True)
    authornotes = models.CharField(max_length=25000, blank=True, null=True)
    directions = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    oldcomments = models.CharField(max_length=50000, blank=True, null=True)
    time_created = models.DateTimeField(auto_now_add=True)


    def get_tag_dict(self, user=None, dedup=True):
        if user is not None:
            try:
                ribbon = Ribbon.objects.get(LiquidRecipes=self, user=user)
                return ribbon.get_tag_dict()
            except ObjectDoesNotExist:
                return {}
        if getattr(self, '_tag_dict', None) is None:
            tags = Tag.objects.filter(ribbon__LiquidRecipes=self)
            tag_dict = {}
            for tag in tags:
                if not tag.key in tag_dict:
                    tag_dict[tag.key] = [tag.value]
                else:
                    tag_dict[tag.key].append(tag.value)
            for key, value in tag_dict.iteritems():
                if dedup:
                    tag_dict[key] = sorted(set(value))
                else:
                    value.sort()

            self._tag_dict = tag_dict
        return self._tag_dict

    def get_used_count(self):
        count = 0
        for ribbon in self.ribbon_set.all():
            if ribbon.is_used:
                count += 1
        return count

    def get_thumbs_up_count(self):
        count = 0
        for ribbon in self.ribbon_set.all():
            if ribbon.thumb == True:
                count += 1
        return count

    def get_thumbs_down_count(self):
        count = 0
        for ribbon in self.ribbon_set.all():
            if ribbon.thumb == False:
                count += 1
        return count

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.link == '':
            self.link = None
        super(LiquidRecipes, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-time_created']


class Ribbon(models.Model):
    LiquidRecipes = models.ForeignKey(LiquidRecipes)
    user = models.ForeignKey(User)
    comments = models.TextField(
            blank=True, null=True,verbose_name="private comments")
    time_created = models.DateTimeField(auto_now_add=True)

    is_boxed = models.BooleanField(
            default=False, verbose_name="Save a Copy")
    boxed_on = models.DateTimeField(blank=True, null=True)
    is_used = models.BooleanField(
            default=False, verbose_name="Have you made this recipe?")

    THUMB_CHOICES = (
        (True, 'Thumbs Up'),
        (False, 'Thumbs Down'),
        )
    thumb = models.NullBooleanField(
            blank=True, null=True, choices=THUMB_CHOICES,
            verbose_name="Would you make it again?")

    def get_tag_dict(self):
        if getattr(self, '_tag_dict', None) is None:
            tags = self.tag_set.all()
            tag_dict = {}
            for tag in tags:
                if not tag.key in tag_dict:
                    tag_dict[tag.key] = [tag.value]
                else:
                    tag_dict[tag.key].append(tag.value)
            for value in tag_dict.itervalues():
                value.sort()
            self._tag_dict = tag_dict
        return self._tag_dict

    def __unicode__(self):
        return u'{0} Ribbon for {1}'.format(unicode(self.LiquidRecipes),
                                           unicode(self.user))

    class Meta:
        unique_together = ('LiquidRecipes', 'user', 'ufid')
        ordering = ['-time_created']


class Tag(models.Model):
    ribbon = models.ForeignKey(Ribbon)
    key = models.CharField(max_length=50)
    value = models.CharField(max_length=50, blank=True, null=True)

    def __unicode__(self):
        return u'{0}: {1}'.format(self.key, self.value)
