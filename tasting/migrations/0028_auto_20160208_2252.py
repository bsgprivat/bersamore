# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasting', '0027_taster_receieve_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='taster',
            name='allow_sysbol_fetch',
            field=models.BooleanField(default=False, help_text='Allow BMS to fetch your orderlists'),
        ),
        migrations.AddField(
            model_name='taster',
            name='untappd_id',
            field=models.CharField(max_length=512, null=True, blank=True),
        ),
    ]
