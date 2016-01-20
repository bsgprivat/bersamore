# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cellar', '0013_auto_20160120_2048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='flag',
        ),
        migrations.AlterField(
            model_name='country',
            name='flag_url',
            field=models.CharField(max_length=256, default='noflag', null=True, blank=True),
        ),
    ]
