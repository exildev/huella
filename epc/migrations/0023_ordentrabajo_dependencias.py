# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-22 23:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epc', '0022_ordentrabajo_nombre_corto'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordentrabajo',
            name='dependencias',
            field=models.ManyToManyField(to='epc.OrdenTrabajo'),
        ),
    ]