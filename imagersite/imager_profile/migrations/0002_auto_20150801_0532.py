# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imager_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagerprofile',
            name='photography_type',
            field=models.CharField(help_text=b'What type of photography do you primaliry make?', max_length=64, choices=[(b'Abstract', b'Abstract'), (b'Animal', b'Animal'), (b'Artistic', b'Artistic'), (b'Beauty', b'Beauty'), (b'Fashion', b'Fashion'), (b'Landscape', b'Landscape'), (b'Nature', b'Nature'), (b'People', b'People'), (b'Travel', b'Travel'), (b'Wedding', b'Wedding')]),
        ),
    ]
