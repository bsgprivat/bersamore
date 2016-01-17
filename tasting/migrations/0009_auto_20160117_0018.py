# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasting', '0008_remove_tastingbeers_pos'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='tastingbeers',
            unique_together=set([('beer', 'tasting')]),
        ),
    ]
