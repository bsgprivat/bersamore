# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasting', '0009_auto_20160117_0018'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checkin',
            old_name='smell',
            new_name='nose',
        ),
    ]
