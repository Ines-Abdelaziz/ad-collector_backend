# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2022-07-05 14:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StoreToDB', '0009_auto_20220705_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_email',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_name',
            field=models.TextField(),
        ),
    ]
