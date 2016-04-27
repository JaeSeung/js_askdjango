# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-16 06:38
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20160416_0603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('^01[016789][1-9]\\d{6,7}$', message='please enter phone_number')]),
        ),
    ]