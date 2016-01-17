# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasting', '0014_taster_friends'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taster',
            name='fav_beers',
            field=models.ManyToManyField(to='cellar.Beer', blank=True),
        ),
        migrations.AlterField(
            model_name='taster',
            name='fav_breweries',
            field=models.ManyToManyField(to='cellar.Brewery', blank=True),
        ),
        migrations.AlterField(
            model_name='taster',
            name='fav_styles',
            field=models.ManyToManyField(to='cellar.Style', blank=True),
        ),
    ]
