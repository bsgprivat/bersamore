# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasting', '0025_taster_public'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taster',
            name='friends',
            field=models.ManyToManyField(related_name='tasterfriends', to='tasting.Taster', blank=True),
        ),
    ]
