# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasting', '0012_tastingsession_finished'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checkin',
            old_name='description',
            new_name='notes',
        ),
    ]
