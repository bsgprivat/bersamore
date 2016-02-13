# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasting', '0028_auto_20160208_2252'),
    ]

    operations = [
        migrations.AddField(
            model_name='taster',
            name='untappd_token',
            field=models.CharField(max_length=512, null=True, blank=True),
        ),
    ]
