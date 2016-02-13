# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imports', '0008_importedbeer_realease'),
    ]

    operations = [
        migrations.AlterField(
            model_name='importedbeer',
            name='thumb_image_url',
            field=models.CharField(default='https//static.systembolaget.se/content/assets/images/products/thumbnail_noimage.png', max_length=512, null=True, help_text='image url', blank=True),
        ),
    ]
