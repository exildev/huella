# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-21 05:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('epc', '0014_actividad_fecha_estimada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividad',
            name='fecha_estimada',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 21, 5, 21, 26, 920393, tzinfo=utc)),
            preserve_default=False,
        ),
    ]