# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cellar', '0028_auto_20160217_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beer',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to='static/images/uploads/beers/thumbnails/', blank=True),
        ),
    ]
