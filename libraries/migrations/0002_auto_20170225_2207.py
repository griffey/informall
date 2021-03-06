# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-25 22:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraries', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='latitude',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='news',
            name='longitude',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='state',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
