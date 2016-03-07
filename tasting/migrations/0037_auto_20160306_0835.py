# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tasting', '0036_auto_20160305_2230'),
    ]

    operations = [
        migrations.AddField(
            model_name='friendship',
            name='date_accepted',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='friendship',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 6, 8, 35, 15, 304254, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
