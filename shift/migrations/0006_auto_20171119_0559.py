# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-19 05:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shift', '0005_auto_20171119_0554'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='run',
            name='shift',
        ),
        migrations.DeleteModel(
            name='Run',
        ),
        migrations.DeleteModel(
            name='Shift',
        ),
    ]
