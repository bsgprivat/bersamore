# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cellar', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='beer',
            name='abv',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='beer',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='beer',
            name='ibu',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='beer',
            name='collabs',
            field=models.ManyToManyField(help_text='Collaborating breweries', related_name='collabs', to='cellar.Brewery', blank=True),
        ),
    ]
