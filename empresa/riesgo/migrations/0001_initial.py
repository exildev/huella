# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-23 01:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CargoRiesgo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acceso', models.IntegerField(blank=True, default=0, null=True)),
                ('impacto', models.IntegerField(blank=True, default=0, null=True)),
                ('contacto_aproteger', models.IntegerField(blank=True, default=0, null=True)),
                ('manejo_programas', models.IntegerField(blank=True, default=0, null=True)),
                ('incidencia_medidas', models.IntegerField(blank=True, default=0, null=True)),
                ('ponderacion', models.FloatField(blank=True, default=0, null=True)),
                ('calificacion', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Criticidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ElementoProteger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='EvaluacionEmpresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('aprobado', models.BooleanField(default=False)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.Empresa')),
            ],
        ),
        migrations.CreateModel(
            name='EvaluacionRiesgos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fuente', models.TextField()),
                ('medio', models.TextField()),
                ('persona', models.TextField()),
                ('metodo', models.TextField()),
                ('probabilidad', models.IntegerField(choices=[(1, b'Raro'), (2, b'Improbable'), (3, b'Posible'), (4, b'Probable'), (5, b'Casi seguro')])),
                ('consecuencia', models.IntegerField(choices=[(1, b'Insignificacnte'), (2, b'Menor'), (3, b'Moderada'), (4, b'Mayor'), (5, b'Catastr\xc3\xb3fica')])),
                ('controles_administrativos', models.TextField()),
                ('controles_operacionales', models.TextField()),
                ('controles_talentoHumano', models.TextField()),
                ('controles_instalacion', models.TextField()),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='riesgo.EvaluacionEmpresa')),
            ],
        ),
        migrations.CreateModel(
            name='Riesgo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amenaza', models.TextField(blank=True)),
                ('riesgo', models.TextField(blank=True)),
                ('aproteger', models.ManyToManyField(blank=True, to='riesgo.ElementoProteger')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.Empresa')),
            ],
        ),
        migrations.AddField(
            model_name='evaluacionriesgos',
            name='riesgo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='riesgo.Riesgo'),
        ),
        migrations.AddField(
            model_name='cargoriesgo',
            name='aproteger',
            field=models.ManyToManyField(blank=True, to='riesgo.ElementoProteger'),
        ),
        migrations.AddField(
            model_name='cargoriesgo',
            name='cargo',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='empresa.Cargo'),
        ),
        migrations.AddField(
            model_name='cargoriesgo',
            name='criticidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='riesgo.Criticidad'),
        ),
    ]
