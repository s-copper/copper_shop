# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-01 19:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['name', 'available'], 'verbose_name_plural': 'Продукты'},
        ),
    ]
