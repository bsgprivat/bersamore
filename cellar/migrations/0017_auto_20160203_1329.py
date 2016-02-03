# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cellar', '0016_foreignid'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='foreignid',
            unique_together=set([('beer', 'source')]),
        ),
    ]
