# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-02 03:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('epc', '0005_auto_20161001_2205'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ordentrabajo',
            old_name='contratista',
            new_name='personal',
        ),
    ]
