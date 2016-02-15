# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasting', '0033_auto_20160215_0511'),
    ]

    operations = [
        migrations.RenameField(
            model_name='taster',
            old_name='allow_contatcs',
            new_name='allow_contacts',
        ),
    ]
