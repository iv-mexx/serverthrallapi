# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-05-14 06:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_clean_data_schema'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='max_players',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='server',
            name='query_port',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='server',
            name='tick_rate',
            field=models.IntegerField(null=True),
        ),
    ]
