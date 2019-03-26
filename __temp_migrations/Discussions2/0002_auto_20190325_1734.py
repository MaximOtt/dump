# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-03-25 16:34
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('Discussions2', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='my_group_int_variable',
        ),
        migrations.RemoveField(
            model_name='player',
            name='my_player_int_variable',
        ),
        migrations.AddField(
            model_name='group',
            name='BeautyGroupResult',
            field=otree.db.models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='BeautyChangeHistory',
            field=otree.db.models.StringField(max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='BeautyCurrentAnswer',
            field=otree.db.models.IntegerField(null=True, verbose_name=''),
        ),
        migrations.AddField(
            model_name='player',
            name='BeautyFirstAnswer',
            field=otree.db.models.IntegerField(null=True, verbose_name=''),
        ),
    ]