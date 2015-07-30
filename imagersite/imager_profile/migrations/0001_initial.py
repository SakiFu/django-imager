# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagerProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('camera', models.CharField(help_text=b'What is model of your camera?', max_length=128)),
                ('address', models.TextField()),
                ('website_url', models.URLField()),
                ('photography_type', models.CharField(help_text=b'What type of photography do you primaliry make?', max_length=64, choices=[(b'AB', b'Abstract'), (b'AN', b'Animal'), (b'AR', b'Artistic'), (b'BE', b'Beauty'), (b'FA', b'Fashion'), (b'LA', b'Landscape'), (b'NA', b'Nature'), (b'PE', b'People'), (b'TR', b'Travel'), (b'WE', b'Wedding')])),
                ('user', models.OneToOneField(related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]