# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cellar', '0010_uploadeduntappdcsv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beer',
            name='sysbol_url',
            field=models.URLField(help_text='systembolaget url', blank=True),
        ),
        migrations.AlterField(
            model_name='brewery',
            name='url',
            field=models.URLField(help_text='Brewery site url', blank=True),
        ),
    ]
