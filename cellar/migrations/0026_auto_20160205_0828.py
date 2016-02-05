# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasting', '0024_auto_20160205_0050'),
        ('cellar', '0025_auto_20160205_0823'),
    ]

    operations = [
        migrations.CreateModel(
            name='BottleSharing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('admin', models.ForeignKey(related_name='bottleshare_admin', to='tasting.Taster')),
                ('participants', models.ManyToManyField(related_name='bottleshare_participant', to='tasting.Taster')),
            ],
        ),
        migrations.AlterField(
            model_name='sysbolorders',
            name='friends',
            field=models.ForeignKey(to='cellar.BottleSharing', null=True),
        ),
        migrations.AlterField(
            model_name='sysbolorders',
            name='nr',
            field=models.IntegerField(help_text='Sysbol order number', null=True, blank=True),
        ),
    ]
