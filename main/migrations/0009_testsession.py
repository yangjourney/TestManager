# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-13 00:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0008_testresult'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('areas_tested', models.TextField(blank=True)),
                ('notes', models.TextField()),
                ('execution_date', models.DateTimeField(editable=False)),
                ('test_charter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.TestCharter')),
                ('test_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.TestGroup')),
                ('tester', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
