# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasting', '0019_tastingbeers_index'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tastingbeers',
            old_name='index',
            new_name='position',
        ),
    ]
