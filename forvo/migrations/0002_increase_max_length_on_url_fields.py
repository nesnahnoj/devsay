# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-04 22:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forvo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forvopronunciation',
            name='path_mp3',
            field=models.URLField(max_length=350),
        ),
        migrations.AlterField(
            model_name='forvopronunciation',
            name='path_ogg',
            field=models.URLField(max_length=350),
        ),
    ]
