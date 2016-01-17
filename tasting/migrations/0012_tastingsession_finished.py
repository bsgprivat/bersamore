# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasting', '0011_auto_20160117_1142'),
    ]

    operations = [
        migrations.AddField(
            model_name='tastingsession',
            name='finished',
            field=models.BooleanField(default=False),
        ),
    ]
