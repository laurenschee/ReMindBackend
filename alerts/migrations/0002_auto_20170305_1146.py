# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-03-05 16:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='alert',
            options={'ordering': ('created_at',), 'permissions': ('readonly', 'Can Read Only Cars')},
        ),
    ]
