# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cellar', '0017_auto_20160203_1329'),
    ]

    operations = [
        migrations.AddField(
            model_name='beer',
            name='year',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
