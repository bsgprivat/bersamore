# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cellar', '0009_brewery_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedUntappdCSV',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('csv_file', models.FileField(upload_to='static/files/uploads/csv')),
            ],
        ),
    ]
