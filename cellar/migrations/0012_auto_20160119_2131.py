# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cellar', '0011_auto_20160117_2314'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='beer',
            unique_together=set([('name', 'brewery')]),
        ),
    ]
