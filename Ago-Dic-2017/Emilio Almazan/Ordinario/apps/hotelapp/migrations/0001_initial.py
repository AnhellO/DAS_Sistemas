# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('fecha_nacimiento', models.DateField()),
                ('email', models.CharField(max_length=50)),
                ('habitacion', models.CharField(max_length=50)),
                ('hotel_hospedaje', models.ForeignKey(blank=True, null=True, to='hotelapp.Sucursal')),
            ],
        ),
    ]
