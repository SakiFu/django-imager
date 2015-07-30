# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imager_images', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='published',
            field=models.CharField(default=b'private', max_length=256, choices=[(b'private', b'private'), (b'shared', b'shared'), (b'public', b'public')]),
        ),
    ]
