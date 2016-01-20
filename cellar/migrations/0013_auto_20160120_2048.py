# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cellar', '0012_auto_20160119_2131'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='flag_url',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='beer',
            name='image',
            field=models.ImageField(default='static/images/uploads/beers/emptybeer.jpg', null=True, upload_to='static/images/uploads/beers/', blank=True),
        ),
    ]
