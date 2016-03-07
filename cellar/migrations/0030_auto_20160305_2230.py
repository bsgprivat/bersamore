# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cellar', '0029_auto_20160217_2011'),
    ]

    operations = [
        migrations.AddField(
            model_name='beer',
            name='checkin_tot',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='beer',
            name='checkins',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='beerimage',
            name='image',
            field=models.ImageField(default='static/images/uploads/beers/emptybeer.jpg', null=True, upload_to='static/images/uploads/beers/gallery/', blank=True),
        ),
    ]
