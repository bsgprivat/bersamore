# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasting', '0030_checkin_pushed_to_untapppd'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkin',
            name='untappd_id',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
