# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-03-17 14:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0008_citypostage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='citypostage',
            old_name='initial_money',
            new_name='initial_price',
        ),
        migrations.RenameField(
            model_name='citypostage',
            old_name='more_money',
            new_name='more_price',
        ),
    ]
