# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cellar', '0022_auto_20160205_0108'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderRow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('qty', models.IntegerField(default=1)),
                ('beer', models.ForeignKey(to='cellar.Beer')),
            ],
        ),
        migrations.RemoveField(
            model_name='orderedbeer',
            name='beers',
        ),
        migrations.RemoveField(
            model_name='sysbolorders',
            name='ordered_beers',
        ),
        migrations.DeleteModel(
            name='OrderedBeer',
        ),
        migrations.AddField(
            model_name='orderrow',
            name='order',
            field=models.ForeignKey(to='cellar.SysbolOrders'),
        ),
        migrations.AddField(
            model_name='sysbolorders',
            name='orderrows',
            field=models.ManyToManyField(to='cellar.Beer', through='cellar.OrderRow'),
        ),
    ]
