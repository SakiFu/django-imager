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
                ('camera', models.CharField(help_text='What is model of your camera?', max_length=128)),
                ('address', models.TextField()),
                ('website_url', models.URLField()),
                ('photography_type', models.CharField(help_text='What type of photography do you primarily take?', max_length=64, choices=[('AB', 'Abstract'), ('AN', 'Animal'), ('AR', 'Artistic'), ('BE', 'Beauty'), ('FA', 'Fashion'), ('LA', 'Landscape'), ('NA', 'Nature'), ('PE', 'People'), ('TR', 'Travel'), ('WE', 'Wedding')])),
                ('user', models.OneToOneField(related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
