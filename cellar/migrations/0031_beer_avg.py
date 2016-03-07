# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cellar', '0030_auto_20160305_2230'),
    ]

    operations = [
        migrations.AddField(
            model_name='beer',
            name='avg',
            field=models.FloatField(default=0),
        ),
    ]
