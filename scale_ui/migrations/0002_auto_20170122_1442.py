# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-22 14:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scale_ui', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timbanglog',
            name='docstatus',
            field=models.CharField(choices=[('DR', 'Draft'), ('IN', 'Intransit'), ('CO', 'Complete'), ('AC', 'Active'), ('UP', 'Uploaded')], default='IN', max_length=2, verbose_name='Doc Status'),
        ),
    ]
