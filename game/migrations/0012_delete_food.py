# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-11 21:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0011_remove_item_type'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Food',
        ),
    ]
