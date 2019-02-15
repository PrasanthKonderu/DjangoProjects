# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-14 06:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_gift'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='product',
        ),
        migrations.AddField(
            model_name='cart',
            name='cake',
            field=models.ManyToManyField(to='product.Cake'),
        ),
    ]