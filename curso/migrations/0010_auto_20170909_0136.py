# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-09 01:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0009_auto_20170909_0050'),
    ]

    operations = [
        migrations.AddField(
            model_name='prospecto',
            name='latitude',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='prospecto',
            name='longitude',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]