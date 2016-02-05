# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasting', '0024_auto_20160205_0050'),
    ]

    operations = [
        migrations.AddField(
            model_name='taster',
            name='public',
            field=models.BooleanField(default=False),
        ),
    ]
