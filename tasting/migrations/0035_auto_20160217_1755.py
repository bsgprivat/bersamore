# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasting', '0034_auto_20160215_0514'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.AddField(
            model_name='store',
            name='address',
            field=models.CharField(default='xxx', max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='store',
            name='zip_code',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='store_id',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='city',
            name='county',
            field=models.ForeignKey(to='tasting.County'),
        ),
        migrations.AddField(
            model_name='store',
            name='city',
            field=models.ForeignKey(default=0, to='tasting.City'),
            preserve_default=False,
        ),
    ]
