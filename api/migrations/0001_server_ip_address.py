# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-04-24 07:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', 'add_clan_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='ip_address',
            field=models.TextField(default=b''),
        ),
    ]