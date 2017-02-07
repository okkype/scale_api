# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-27 09:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scale_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScaleConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True, verbose_name='Name')),
                ('value', models.CharField(max_length=40, verbose_name='Value')),
            ],
        ),
    ]