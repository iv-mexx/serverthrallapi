# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-05-07 06:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_server_ip_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServerSyncData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('server', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='api.Server')),
            ],
        ),
        migrations.RenameField(
            model_name='clan',
            old_name='owner_id',
            new_name='conan_owner_id',
        ),
        migrations.AddField(
            model_name='character',
            name='clan',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='members', to='api.Clan'),
        ),
        migrations.AddField(
            model_name='clan',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='owner', to='api.Character'),
        ),
        migrations.AlterField(
            model_name='characterhistory',
            name='character',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='history', to='api.Character'),
        ),
        migrations.AlterField(
            model_name='clan',
            name='server',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clans', to='api.Server'),
        ),
    ]
