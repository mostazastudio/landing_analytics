# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-17 22:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prospecto',
            name='apellido',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='prospecto',
            name='nombre',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
