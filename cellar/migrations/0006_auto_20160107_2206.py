# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cellar', '0005_auto_20160107_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beer',
            name='image',
            field=models.ImageField(null=True, upload_to='images/uploads/beers/', blank=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='flag',
            field=models.ImageField(null=True, upload_to='images/uploads/flags/', blank=True),
        ),
    ]
