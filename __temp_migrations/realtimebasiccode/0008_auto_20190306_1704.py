# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-03-06 16:04
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('realtimebasiccode', '0007_auto_20190306_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='my_group_int_variable',
            field=otree.db.models.IntegerField(default=33, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='my_player_int_variable',
            field=otree.db.models.IntegerField(default=11, null=True),
        ),
    ]
