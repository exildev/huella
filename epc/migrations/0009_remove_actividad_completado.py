# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-20 13:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('epc', '0008_auto_20160920_0800'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actividad',
            name='completado',
        ),
    ]