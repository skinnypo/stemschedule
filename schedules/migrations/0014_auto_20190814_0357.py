# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2019-08-14 03:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0013_auto_20190808_0927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeslot',
            name='time_at',
            field=models.CharField(max_length=40),
        ),
    ]
