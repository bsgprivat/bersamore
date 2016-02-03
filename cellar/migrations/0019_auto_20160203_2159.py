# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cellar', '0018_beer_year'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='foreignid',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='foreignid',
            name='beer',
        ),
        migrations.RemoveField(
            model_name='beer',
            name='sysbol_url',
        ),
        migrations.AddField(
            model_name='beer',
            name='sysbol_cart_id',
            field=models.IntegerField(help_text='aka "nr", used to build carts', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='beer',
            name='sysbol_id',
            field=models.IntegerField(help_text='aka "varunummer", used to build urls with', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='beer',
            name='untappd_id',
            field=models.IntegerField(help_text='Untappds unique Beer ID', null=True, blank=True),
        ),
        migrations.DeleteModel(
            name='ForeignID',
        ),
    ]
