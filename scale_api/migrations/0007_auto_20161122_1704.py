# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-22 17:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scale_api', '0006_auto_20161122_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scaleconfig',
            name='name',
            field=models.CharField(choices=[('scale_port', 'Scale Port'), ('scale_baudrate', 'Scale Baudrate'), ('scale_bit_data', 'Scale Bit Data'), ('scale_bit_stop', 'Scale Bit Stop'), ('scale_parity', 'Scale Parity'), ('scale_timeout', 'Scale Timeout'), ('scale_address', 'Scale Address')], max_length=40, null=True, verbose_name='Name'),
        ),
        migrations.AlterUniqueTogether(
            name='scaleconfig',
            unique_together=set([('m_warehouse_id', 'name')]),
        ),
    ]
