# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-12 20:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20170912_2015'),
    ]

    operations = [
        migrations.AddField(
            model_name='galeriaphotos',
            name='detail',
            field=models.TextField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='articulos',
            name='file',
            field=models.FileField(blank=True, max_length=200, null=True, upload_to='articles'),
        ),
        migrations.AlterField(
            model_name='docentes',
            name='photo',
            field=models.ImageField(blank=True, height_field=200, max_length=200, null=True, upload_to='profile_picture', width_field=400),
        ),
        migrations.AlterField(
            model_name='galeriaphotos',
            name='photo',
            field=models.ImageField(blank=True, height_field=300, max_length=200, null=True, upload_to='gallery', width_field=500),
        ),
    ]
