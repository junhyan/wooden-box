# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-23 15:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notebook', '0002_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='passwd',
            field=models.CharField(max_length=50, null=True),
        ),
    ]