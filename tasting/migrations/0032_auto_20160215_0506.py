# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasting', '0031_checkin_untappd_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('store_id', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='taster',
            name='display_email',
        ),
        migrations.AddField(
            model_name='taster',
            name='stores',
            field=models.ManyToManyField(to='tasting.Store', blank=True),
        ),
    ]
