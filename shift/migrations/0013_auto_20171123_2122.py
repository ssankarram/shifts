# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-23 21:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shift', '0012_auto_20171123_1901'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shift',
            name='shiftGroup',
        ),
        migrations.AddField(
            model_name='shift',
            name='shiftGroup',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shifts_related', to='shift.ShiftGroup'),
        ),
    ]