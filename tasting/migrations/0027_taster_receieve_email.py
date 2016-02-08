# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasting', '0026_auto_20160207_2124'),
    ]

    operations = [
        migrations.AddField(
            model_name='taster',
            name='receieve_email',
            field=models.BooleanField(default=True),
        ),
    ]
