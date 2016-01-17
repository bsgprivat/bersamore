# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cellar', '0010_uploadeduntappdcsv'),
        ('tasting', '0006_auto_20160116_2345'),
    ]

    operations = [
        migrations.AddField(
            model_name='tastingsession',
            name='beers',
            field=models.ManyToManyField(to='cellar.Beer', through='tasting.TastingBeers', blank=True),
        ),
    ]
