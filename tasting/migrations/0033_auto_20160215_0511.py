# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasting', '0032_auto_20160215_0506'),
    ]

    operations = [
        migrations.RenameField(
            model_name='taster',
            old_name='allow_contacs',
            new_name='allow_contatcs',
        ),
        migrations.RemoveField(
            model_name='taster',
            name='public',
        ),
    ]
