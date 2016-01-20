# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cellar', '0014_auto_20160120_2052'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='flag_url',
        ),
    ]
