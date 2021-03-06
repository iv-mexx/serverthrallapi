# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-04-23 09:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_clan'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='conan_clan_id',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='server',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='characters', to='api.Server'),
        ),
    ]
