# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-22 16:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scale_api', '0004_auto_20161107_0257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scaleconfig',
            name='created',
        ),
        migrations.RemoveField(
            model_name='scaleconfig',
            name='name',
        ),
        migrations.RemoveField(
            model_name='scaleconfig',
            name='updated',
        ),
        migrations.RemoveField(
            model_name='scaleconfig',
            name='value',
        ),
    ]
