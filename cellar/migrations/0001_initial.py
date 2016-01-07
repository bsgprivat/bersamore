# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='Brewery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('flag', models.ImageField(null=True, upload_to=b'', blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='brewery',
            name='country',
            field=models.ForeignKey(blank=True, to='cellar.Country', null=True),
        ),
        migrations.AddField(
            model_name='beer',
            name='brewery',
            field=models.ForeignKey(blank=True, to='cellar.Brewery', null=True),
        ),
        migrations.AddField(
            model_name='beer',
            name='collabs',
            field=models.ManyToManyField(related_name='collabs', to='cellar.Brewery'),
        ),
    ]
