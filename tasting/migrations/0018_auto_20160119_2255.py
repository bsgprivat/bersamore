# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tasting', '0017_auto_20160119_2228'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkin',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 19, 22, 55, 7, 220954, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tastinginvitation',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Invited'), (1, 'Accepted'), (2, 'Declined')]),
        ),
    ]
