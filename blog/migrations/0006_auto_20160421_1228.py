# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-21 12:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20160417_0726'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='post',
        ),
        migrations.RemoveField(
            model_name='game',
            name='post2',
        ),
    ]