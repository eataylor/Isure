# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-01 18:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Isure', '0031_auto_20161201_0927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='directory',
            name='awards1',
            field=models.TextField(blank=True, max_length=500, verbose_name='Top Awards1'),
        ),
        migrations.AlterField(
            model_name='directory',
            name='awards2',
            field=models.TextField(blank=True, max_length=500, verbose_name='Top Awards2'),
        ),
        migrations.AlterField(
            model_name='directory',
            name='awards3',
            field=models.TextField(blank=True, max_length=500, verbose_name='Top Awards3'),
        ),
        migrations.AlterField(
            model_name='directory',
            name='goals1',
            field=models.TextField(blank=True, max_length=500, verbose_name='Top Goals1'),
        ),
        migrations.AlterField(
            model_name='directory',
            name='goals2',
            field=models.TextField(blank=True, max_length=500, verbose_name='Top Goals2'),
        ),
        migrations.AlterField(
            model_name='directory',
            name='goals3',
            field=models.TextField(blank=True, max_length=500, verbose_name='Top Goals3'),
        ),
    ]
