# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cellar', '0007_auto_20160107_2208'),
        ('tasting', '0002_auto_20160107_2148'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('looks', models.IntegerField(null=True, blank=True)),
                ('smell', models.IntegerField(null=True, blank=True)),
                ('taste', models.IntegerField(null=True, blank=True)),
                ('overall', models.IntegerField(null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('beer', models.ForeignKey(to='cellar.Beer')),
                ('taster', models.ForeignKey(to='tasting.Taster')),
                ('tasting', models.ForeignKey(to='tasting.TastingSession')),
            ],
        ),
    ]
