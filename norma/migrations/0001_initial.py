# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-02 23:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('formulario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Formato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('documento', models.FileField(blank=True, null=True, upload_to=b'formatos')),
                ('ejemplo', models.FileField(blank=True, null=True, upload_to=b'formatos_ejemplo')),
                ('formulario_digital', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='formulario.Formulario')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Norma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('edicion', models.CharField(max_length=50)),
                ('fecha_edicion', models.DateField()),
                ('referencia', models.CharField(max_length=100)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='norma',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='norma.Norma'),
        ),
        migrations.AddField(
            model_name='formato',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='norma.Item'),
        ),
    ]
