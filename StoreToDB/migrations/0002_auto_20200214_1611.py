# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-02-14 16:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StoreToDB', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videoad',
            name='ad_channel_description',
            field=models.CharField(max_length=10000),
        ),
    ]