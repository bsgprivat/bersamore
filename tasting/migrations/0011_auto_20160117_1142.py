# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cellar', '0010_uploadeduntappdcsv'),
        ('tasting', '0010_auto_20160117_0943'),
    ]

    operations = [
        migrations.AddField(
            model_name='taster',
            name='fav_beers',
            field=models.ManyToManyField(to='cellar.Beer'),
        ),
        migrations.AddField(
            model_name='taster',
            name='fav_breweries',
            field=models.ManyToManyField(to='cellar.Brewery'),
        ),
        migrations.AddField(
            model_name='taster',
            name='fav_styles',
            field=models.ManyToManyField(to='cellar.Style'),
        ),
    ]
