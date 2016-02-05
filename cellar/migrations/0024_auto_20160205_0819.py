# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasting', '0024_auto_20160205_0050'),
        ('cellar', '0023_auto_20160205_0754'),
    ]

    operations = [
        migrations.AddField(
            model_name='sysbolorders',
            name='friends',
            field=models.ForeignKey(related_name='bottlesharing', to='tasting.Taster', null=True),
        ),
        migrations.AddField(
            model_name='sysbolorders',
            name='imported',
            field=models.BooleanField(default=False, help_text='Is imported from order history @ systembolaget'),
        ),
        migrations.AddField(
            model_name='sysbolorders',
            name='internal',
            field=models.BooleanField(default=True, help_text='Is created from BMS'),
        ),
    ]
