# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-24 22:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epc', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividad',
            name='fecha_completado',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='actividad',
            name='fecha_estimada',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='fecha_final',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='fecha_inicio',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='ordentrabajo',
            name='fecha',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='ordentrabajo',
            name='fecha_creacion',
            field=models.DateField(auto_now_add=True),
        ),
    ]
