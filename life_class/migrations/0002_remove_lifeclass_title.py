# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-07 06:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('life_class', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lifeclass',
            name='title',
        ),
    ]
