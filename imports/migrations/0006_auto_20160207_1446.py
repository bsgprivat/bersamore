# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imports', '0005_auto_20160207_1400'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='importedbeer',
            name='unavailable',
        ),
        migrations.AddField(
            model_name='importedbeer',
            name='available',
            field=models.BooleanField(default=True),
        ),
    ]
