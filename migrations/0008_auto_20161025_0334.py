# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-25 03:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Isure', '0007_auto_20161025_0238'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'verbose_name_plural': 'Events'},
        ),
        migrations.AlterModelOptions(
            name='quicklinks',
            options={'verbose_name_plural': 'QuickLinks'},
        ),
        migrations.RenameField(
            model_name='event',
            old_name='Eventtext',
            new_name='EventText',
        ),
        migrations.AddField(
            model_name='event',
            name='EventSummary',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
