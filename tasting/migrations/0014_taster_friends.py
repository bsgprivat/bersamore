# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasting', '0013_auto_20160117_1436'),
    ]

    operations = [
        migrations.AddField(
            model_name='taster',
            name='friends',
            field=models.ManyToManyField(related_name='tasterfriends', to='tasting.Taster'),
        ),
    ]
