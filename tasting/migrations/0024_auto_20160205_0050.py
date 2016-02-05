# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasting', '0023_checkin_from_untappd'),
    ]

    operations = [
        migrations.AddField(
            model_name='taster',
            name='sysbol_id',
            field=models.EmailField(help_text='Used to connect against your systembolaget account', max_length=254, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='tastingsession',
            name='administrators',
            field=models.ManyToManyField(related_name='tasting_admin', to='tasting.Taster'),
        ),
    ]
