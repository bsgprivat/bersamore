# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasting', '0035_auto_20160217_1755'),
        ('cellar', '0027_brewery_untappd_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='BeerImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(default='static/images/uploads/beers/emptybeer.jpg', null=True, upload_to='static/images/uploads/beers/', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='UploadedBeerImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('approved', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='beer',
            name='thumbnail',
            field=models.ImageField(default='static/images/uploads/beers/emptybeer.jpg', height_field=90, width_field=45, upload_to='static/images/uploads/beers/thumbnails/', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='beer',
            name='thumbnail_url',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='beer',
            name='sysbol_id',
            field=models.IntegerField(help_text='aka "varunummer", used to build urls', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='uploadedbeerimage',
            name='beer',
            field=models.ForeignKey(to='cellar.Beer'),
        ),
        migrations.AddField(
            model_name='uploadedbeerimage',
            name='image',
            field=models.ForeignKey(to='cellar.BeerImage'),
        ),
        migrations.AddField(
            model_name='uploadedbeerimage',
            name='uploaded_by',
            field=models.ForeignKey(to='tasting.Taster'),
        ),
        migrations.AddField(
            model_name='beer',
            name='gallery',
            field=models.ManyToManyField(to='cellar.BeerImage', through='cellar.UploadedBeerImage', blank=True),
        ),
    ]
