# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasting', '0018_auto_20160119_2255'),
    ]

    operations = [
        migrations.AddField(
            model_name='tastingbeers',
            name='index',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
