# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cellar', '0003_auto_20160107_2155'),
    ]

    operations = [
        migrations.AddField(
            model_name='beer',
            name='image',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
        migrations.AddField(
            model_name='beer',
            name='sysbol_url',
            field=models.URLField(default='http://', help_text='systembolaget url'),
            preserve_default=False,
        ),
    ]
