# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-11 06:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('life_class', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lifeclass',
            name='tags',
            field=models.CharField(default='webly', max_length=50),
            preserve_default=False,
        ),
    ]
