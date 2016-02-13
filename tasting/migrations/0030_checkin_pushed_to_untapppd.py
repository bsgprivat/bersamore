# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasting', '0029_taster_untappd_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkin',
            name='pushed_to_untapppd',
            field=models.BooleanField(default=False),
        ),
    ]
