# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-20 12:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_cake_available'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='catagery',
        ),
    ]
