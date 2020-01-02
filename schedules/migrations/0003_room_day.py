# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2019-02-11 10:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0002_auto_20190211_0359'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='day',
            field=models.DateField(default=None, help_text='Day of the event', verbose_name='Day of the event'),
            preserve_default=False,
        ),
    ]