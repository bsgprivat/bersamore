# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasting', '0015_auto_20160117_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkin',
            name='tasting',
            field=models.ForeignKey(blank=True, to='tasting.TastingSession', null=True),
        ),
    ]
