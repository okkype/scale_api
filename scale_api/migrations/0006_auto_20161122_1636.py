# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-22 16:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('scale_api', '0005_auto_20161122_1610'),
    ]

    operations = [
        migrations.AddField(
            model_name='scaleconfig',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scaleconfig',
            name='m_warehouse_id',
            field=models.IntegerField(null=True, verbose_name='Warehouse'),
        ),
        migrations.AddField(
            model_name='scaleconfig',
            name='name',
            field=models.CharField(choices=[('scale_port', 'Scale Port'), ('scale_baudrate', 'Scale Baudrate'), ('scale_bit_data', 'Scale Bit Data'), ('scale_bit_stop', 'Scale Bit Stop'), ('scale_parity', 'Scale Parity'), ('scale_timeout', 'Scale Timeout'), ('scale_address', 'Scale Address')], max_length=40, null=True, unique=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='scaleconfig',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='scaleconfig',
            name='value',
            field=models.CharField(max_length=40, null=True, verbose_name='Value'),
        ),
    ]
