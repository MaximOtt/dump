# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-03-06 14:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realtimebasiccode', '0005_remove_player_my_player_chr_variable'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='my_group_chr_variable',
        ),
    ]
