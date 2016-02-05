# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasting', '0022_auto_20160203_1329'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkin',
            name='from_untappd',
            field=models.BooleanField(default=False),
        ),
    ]
