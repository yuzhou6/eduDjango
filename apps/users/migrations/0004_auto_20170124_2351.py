# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-01-24 23:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20170124_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='nick_name',
            field=models.CharField(default='', max_length=50, verbose_name='\u6635\u79f0'),
        ),
    ]
