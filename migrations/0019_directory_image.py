# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-31 04:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Isure', '0018_auto_20161031_0052'),
    ]

    operations = [
        migrations.AddField(
            model_name='directory',
            name='Image',
            field=models.FileField(default='', upload_to='Pics'),
            preserve_default=False,
        ),
    ]
