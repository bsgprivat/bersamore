# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasting', '0016_auto_20160119_2215'),
    ]

    operations = [
        migrations.CreateModel(
            name='TastingInvitation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.IntegerField(choices=[(0, 'Invited'), (1, 'Accepted'), (2, 'Declined')])),
                ('taster', models.ForeignKey(to='tasting.Taster')),
                ('tasting', models.ForeignKey(to='tasting.TastingSession')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='tastinginvitation',
            unique_together=set([('taster', 'tasting')]),
        ),
    ]
