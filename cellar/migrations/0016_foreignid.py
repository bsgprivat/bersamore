# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cellar', '0015_remove_country_flag_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='ForeignID',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('u_id', models.CharField(max_length=255)),
                ('source', models.IntegerField(choices=[(0, 'Systembolaget'), (1, 'Untappd'), (2, 'Boxbeers'), (3, 'Ratebeer'), (4, 'BeerAdvocate')])),
                ('beer', models.ForeignKey(to='cellar.Beer')),
            ],
        ),
    ]
