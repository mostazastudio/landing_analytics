# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-25 22:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0006_remove_prospecto_source'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prospecto',
            name='apellido',
        ),
    ]