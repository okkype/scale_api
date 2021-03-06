# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-23 09:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scale_api', '0007_auto_20161122_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scaleconfig',
            name='name',
            field=models.CharField(choices=[('scale_port', 'Scale Port'), ('scale_baudrate', 'Scale Baudrate'), ('scale_bit_data', 'Scale Bit Data'), ('scale_bit_stop', 'Scale Bit Stop'), ('scale_parity', 'Scale Parity'), ('scale_timeout', 'Scale Timeout'), ('scale_address', 'Scale Address'), ('scale_uom_id', 'Scale UoM ID')], max_length=40, null=True, verbose_name='Name'),
        ),
    ]
