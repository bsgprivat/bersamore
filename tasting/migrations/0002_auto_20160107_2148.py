# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasting', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tastingsession',
            name='beers',
            field=models.ManyToManyField(to='cellar.Beer'),
        ),
        migrations.AlterField(
            model_name='tastingsession',
            name='tasters',
            field=models.ManyToManyField(to='tasting.Taster'),
        ),
    ]
