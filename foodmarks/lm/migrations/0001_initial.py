# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-16 16:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('link', models.URLField(blank=True, max_length=255, null=True, unique=True)),
                ('servings', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('ingredients', models.TextField(blank=True, null=True)),
                ('directions', models.TextField(blank=True, null=True)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-time_created'],
            },
        ),
        migrations.CreateModel(
            name='Ribbon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.TextField(blank=True, null=True, verbose_name=b'my comments')),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('is_boxed', models.BooleanField(default=False, verbose_name=b'Include in your Recipe Box?')),
                ('boxed_on', models.DateTimeField(blank=True, null=True)),
                ('is_used', models.BooleanField(default=False, verbose_name=b'Have you used this recipe?')),
                ('thumb', models.NullBooleanField(choices=[(True, b'Thumbs Up'), (False, b'Thumbs Down')], verbose_name=b"How's the recipe?")),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fm.Recipe')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-time_created'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=50)),
                ('value', models.CharField(blank=True, max_length=50, null=True)),
                ('ribbon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fm.Ribbon')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='ribbon',
            unique_together=set([('recipe', 'user')]),
        ),
    ]
