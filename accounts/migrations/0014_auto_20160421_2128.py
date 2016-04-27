# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-21 21:28
from __future__ import unicode_literals

import accounts.models
import django.core.validators
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20160421_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=accounts.models.PhoneNumberField(max_length=20, validators=[django.core.validators.RegexValidator('^01[016789][1-9]\\d{6,7}$', message='please enter phone_number'), django.core.validators.RegexValidator('^01[016789][1-9]\\d{6,7}$', message='please enter phone_number'), django.core.validators.RegexValidator('^01[016789][1-9]\\d{6,7}$', message='please enter phone_number')]),
        ),
    ]
