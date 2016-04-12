# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-25 17:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oppia', '0009_auto_20150524_0223')
    ]

    database_operations = [
        migrations.AlterModelTable(
            name='UserProfile',
            table='profile_userprofile'
        )
    ]

    state_operations = [
        migrations.DeleteModel('UserProfile')
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=database_operations,
            state_operations=state_operations)
    ]
