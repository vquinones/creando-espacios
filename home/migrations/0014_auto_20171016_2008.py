# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-16 20:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_docentes_publico'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulos',
            name='publico',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='eventos',
            name='publico',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='galeria',
            name='publico',
            field=models.BooleanField(default=False),
        ),
    ]
