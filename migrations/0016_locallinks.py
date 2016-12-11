# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-30 00:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Isure', '0015_auto_20161029_1825'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocalLinks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postDate', models.DateField()),
                ('blurb', models.CharField(max_length=250)),
                ('link', models.CharField(max_length=50)),
                ('publish', models.BooleanField()),
            ],
            options={
                'verbose_name_plural': 'Local Links',
            },
        ),
    ]
