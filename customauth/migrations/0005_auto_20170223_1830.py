# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-23 13:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customauth', '0004_auto_20170223_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citizen',
            name='phone',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]