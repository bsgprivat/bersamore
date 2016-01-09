# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-09 00:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cellar', '0007_auto_20160107_2208'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hops',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
            ],
            options={
                'verbose_name_plural': 'hops',
            },
        ),
        migrations.CreateModel(
            name='Style',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
            ],
        ),
        migrations.AddField(
            model_name='country',
            name='code',
            field=models.CharField(default='se', max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='country',
            name='flag',
            field=models.ImageField(blank=True, help_text='Use "country-code.png"', null=True, upload_to='static/images/uploads/flags/'),
        ),
        migrations.AddField(
            model_name='hops',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cellar.Country'),
        ),
        migrations.AddField(
            model_name='beer',
            name='hops',
            field=models.ManyToManyField(blank=True, to='cellar.Hops'),
        ),
        migrations.AddField(
            model_name='beer',
            name='style',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cellar.Style'),
        ),
    ]
