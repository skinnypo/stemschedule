# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2019-08-14 07:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0016_auto_20190814_0705'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ClassSlot',
            new_name='RoomSlot',
        ),
    ]
