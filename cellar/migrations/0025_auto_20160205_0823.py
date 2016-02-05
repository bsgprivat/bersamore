# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cellar', '0024_auto_20160205_0819'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderrow',
            name='cancelled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='orderrow',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='orderrow',
            name='sent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='sysbolorders',
            name='order_arrived',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='sysbolorders',
            name='order_picked_up',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
