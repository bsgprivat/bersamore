# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imports', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='importedbeer',
            name='batch_size',
            field=models.IntegerField(help_text='Only sold in batches', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='importedbeer',
            name='cant_be_ordered',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='importedbeer',
            name='sysbol_price',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='importedbeer',
            name='sysbol_price_checked_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='importedbeer',
            name='url',
            field=models.CharField(help_text='url to product', max_length=512, null=True, blank=True),
        ),
    ]
