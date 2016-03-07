# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasting', '0035_auto_20160217_1755'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friendship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.IntegerField(default=0, choices=[(0, 'Invited'), (1, 'Accepted'), (2, 'Declined')])),
                ('inviter', models.ForeignKey(related_name='friend_inviter', to='tasting.Taster')),
                ('receiver', models.ForeignKey(related_name='friend_receiver', to='tasting.Taster')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='friendship',
            unique_together=set([('inviter', 'receiver')]),
        ),
    ]
