# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-12-11 21:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_auto_20181211_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodpost',
            name='foodPic',
            field=models.ImageField(blank=True, default='', null=True, upload_to=''),
        ),
    ]
