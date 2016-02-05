# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasting', '0024_auto_20160205_0050'),
        ('cellar', '0019_auto_20160203_2159'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='StockedBeer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('purchase_date', models.DateTimeField(null=True, blank=True)),
                ('best_before_date', models.DateTimeField(null=True, blank=True)),
                ('location', models.CharField(max_length=255, null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='beer',
            name='ean',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='stockedbeer',
            name='beer',
            field=models.ForeignKey(to='cellar.Beer'),
        ),
        migrations.AddField(
            model_name='stockedbeer',
            name='user',
            field=models.ForeignKey(to='tasting.Taster'),
        ),
        migrations.AddField(
            model_name='orders',
            name='beers',
            field=models.ManyToManyField(to='cellar.Beer'),
        ),
    ]
