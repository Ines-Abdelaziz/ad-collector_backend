# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2022-02-10 10:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StoreToDB', '0007_auto_20200218_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='floatingad',
            name='host_video_link',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='user',
            name='country',
            field=models.CharField(default='', max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='videoad',
            name='host_video_link',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]