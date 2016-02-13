# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cellar', '0026_auto_20160205_0828'),
    ]

    operations = [
        migrations.AddField(
            model_name='brewery',
            name='untappd_id',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
