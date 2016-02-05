# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cellar', '0020_auto_20160205_0050'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderedBeer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('qty', models.IntegerField(default=1)),
                ('beers', models.ManyToManyField(to='cellar.Beer')),
            ],
        ),
        migrations.CreateModel(
            name='SysbolOrders',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nr', models.IntegerField(help_text='Sysbol order number')),
                ('order_made', models.DateTimeField()),
                ('ordered_beers', models.ManyToManyField(to='cellar.OrderedBeer', null=True, blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='orders',
            name='beers',
        ),
        migrations.DeleteModel(
            name='Orders',
        ),
    ]
