# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imports', '0007_importedbeer_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='importedbeer',
            name='realease',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
