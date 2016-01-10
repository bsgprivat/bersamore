# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasting', '0004_auto_20160107_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkin',
            name='description',
            field=models.TextField(max_length=300, null=True, blank=True),
        ),
    ]
