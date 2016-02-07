# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imports', '0003_auto_20160207_1001'),
    ]

    operations = [
        migrations.AddField(
            model_name='importedbeer',
            name='unavailable',
            field=models.BooleanField(default=False),
        ),

    ]
