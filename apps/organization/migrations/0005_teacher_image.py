# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-02-03 15:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0004_auto_20170202_2200'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='image',
            field=models.ImageField(default='', upload_to='teacher/%Y/%m', verbose_name='\u5934\u50cf'),
        ),
    ]
