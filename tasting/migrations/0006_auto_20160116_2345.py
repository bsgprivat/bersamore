# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cellar', '0010_uploadeduntappdcsv'),
        ('tasting', '0005_auto_20160109_2328'),
    ]

    operations = [
        migrations.CreateModel(
            name='TastingBeers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pos', models.IntegerField(default=0)),
                ('beer', models.ForeignKey(to='cellar.Beer')),
            ],
        ),
        migrations.RemoveField(
            model_name='tastingsession',
            name='beers',
        ),
        migrations.AddField(
            model_name='tastingbeers',
            name='tasting',
            field=models.ForeignKey(to='tasting.TastingSession'),
        ),
    ]
