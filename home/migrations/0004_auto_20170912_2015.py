# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-12 20:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20170911_0313'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articulos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=60)),
                ('detail', models.TextField(default='', max_length=500)),
                ('file', models.FileField(blank=True, max_length=200, null=True, upload_to='static/profile_picture')),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.AlterField(
            model_name='docentes',
            name='photo',
            field=models.FileField(blank=True, max_length=200, null=True, upload_to='static/profile_picture'),
        ),
        migrations.AlterField(
            model_name='galeriaphotos',
            name='photo',
            field=models.FileField(blank=True, max_length=200, null=True, upload_to='static/gallery'),
        ),
    ]
