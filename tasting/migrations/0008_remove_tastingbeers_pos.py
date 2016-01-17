# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasting', '0007_tastingsession_beers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tastingbeers',
            name='pos',
        ),
    ]
