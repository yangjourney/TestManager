# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-04 19:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_defect'),
    ]

    operations = [
        migrations.AlterField(
            model_name='defect',
            name='affected_test_cases',
            field=models.ManyToManyField(blank=True, to='main.TestCase'),
        ),
    ]
