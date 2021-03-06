# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-16 17:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='todolist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=20)),
                ('Description', models.CharField(max_length=225)),
                ('datetime', models.DateTimeField()),
                ('Status', models.CharField(choices=[('Inprogress', 'In progress'), ('completed', 'completed'), ('pending', 'pending')], max_length=250)),
                ('Createdat', models.DateTimeField(auto_now_add=True)),
                ('Modifiedat', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'todolist',
            },
        ),
    ]
