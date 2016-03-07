# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cellar', '0031_beer_avg'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='beer',
            name='checkin_tot',
        ),
        migrations.RemoveField(
            model_name='beer',
            name='checkins',
        ),
    ]
