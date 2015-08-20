# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_modified', models.DateField(auto_now=True)),
                ('date_published', models.DateField(null=True, blank=True)),
                ('published', models.CharField(default=b'private', max_length=256, choices=[(b'private', b'private'), (b'shared', b'shared'), (b'public', b'public')])),
            ],
        ),
        migrations.CreateModel(
            name='Face',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128, null=True, blank=True)),
                ('x', models.IntegerField()),
                ('y', models.IntegerField()),
                ('height', models.IntegerField()),
                ('width', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'photo_files/%Y-%m-%d')),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_modified', models.DateField(auto_now=True)),
                ('date_published', models.DateField(auto_now=True)),
                ('published', models.CharField(default=b'private', max_length=256, choices=[(b'private', b'private'), (b'shared', b'shared'), (b'public', b'public')])),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326, null=True, verbose_name=b'location', blank=True)),
                ('user', models.ForeignKey(related_name='photos', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='face',
            name='photo',
            field=models.ForeignKey(related_name='faces', to='imager_images.Photo'),
        ),
        migrations.AddField(
            model_name='album',
            name='cover',
            field=models.ForeignKey(related_name='cover_for', blank=True, to='imager_images.Photo', null=True),
        ),
        migrations.AddField(
            model_name='album',
            name='photos',
            field=models.ManyToManyField(related_name='albums', to='imager_images.Photo', blank=True),
        ),
        migrations.AddField(
            model_name='album',
            name='user',
            field=models.ForeignKey(related_name='albums', to=settings.AUTH_USER_MODEL),
        ),
    ]
