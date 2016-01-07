# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cellar', '0002_auto_20160107_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beer',
            name='description',
            field=models.TextField(null=True, blank=True),
        ),
    ]
