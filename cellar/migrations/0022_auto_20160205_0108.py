# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasting', '0024_auto_20160205_0050'),
        ('cellar', '0021_auto_20160205_0059'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stockedbeer',
            old_name='user',
            new_name='taster',
        ),
        migrations.AddField(
            model_name='sysbolorders',
            name='taster',
            field=models.ForeignKey(default=None, to='tasting.Taster'),
            preserve_default=False,
        ),
    ]
