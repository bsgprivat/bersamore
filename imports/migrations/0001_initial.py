# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImportedBeer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Name of beer', max_length=512, null=True, blank=True)),
                ('image_url', models.CharField(default='static/images/uploads/beers/emptybeer.jpg', max_length=512, null=True, help_text='image url', blank=True)),
                ('thumb_image_url', models.CharField(default='static/images/uploads/beers/emptybeer.jpg', max_length=512, null=True, help_text='image url', blank=True)),
                ('brewery', models.CharField(help_text='Name of Brewery', max_length=512, null=True, blank=True)),
                ('collabs', models.CharField(help_text='Collaborating breweries', max_length=512, null=True, blank=True)),
                ('abv', models.FloatField(default=0.0)),
                ('ibu', models.IntegerField(default=0)),
                ('description', models.TextField(null=True, blank=True)),
                ('year', models.IntegerField(null=True, blank=True)),
                ('ean', models.IntegerField(null=True, blank=True)),
                ('sysbol_id', models.IntegerField(help_text='aka "varunummer", used to build urls with', null=True, blank=True)),
                ('sysbol_cart_id', models.IntegerField(help_text='aka "nr", used to build carts', null=True, blank=True)),
            ],
        ),
    ]
