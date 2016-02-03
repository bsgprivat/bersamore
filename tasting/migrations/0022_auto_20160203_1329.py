# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasting', '0021_auto_20160128_2310'),
    ]

    operations = [
        migrations.AddField(
            model_name='taster',
            name='allow_contacs',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='taster',
            name='display_email',
            field=models.BooleanField(default=False),
        ),
    ]
