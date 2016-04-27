# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-23 06:58
from __future__ import unicode_literals

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_delete_game'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200, validators=[blog.models.validator_even_length]),
        ),
    ]
