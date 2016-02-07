# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imports', '0002_auto_20160207_0953'),
    ]

    operations = [
        migrations.AddField(
            model_name='importedbeer',
            name='country',
            field=models.CharField(max_length=128, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='importedbeer',
            name='image_url',
            field=models.CharField(help_text='image url', max_length=512, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='importedbeer',
            name='thumb_image_url',
            field=models.CharField(help_text='image url', max_length=512, null=True, blank=True),
        ),
    ]
