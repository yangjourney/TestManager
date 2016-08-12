# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-04 19:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_auto_20160804_1811'),
    ]

    operations = [
        migrations.CreateModel(
            name='Defect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('Open', 'Open'), ('In-work', 'In-work'), ('Fixed', 'Fixed'), ('In-test', 'In-test'), ('Closed', 'Closed')], max_length=15)),
                ('priority', models.CharField(choices=[('Critical', 'Critical'), ('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')], max_length=15)),
                ('procedure', models.TextField()),
                ('affected_test_cases', models.ManyToManyField(to='main.TestCase')),
                ('affected_versions', models.ManyToManyField(blank=True, related_name='affected_versions', to='main.Version')),
                ('assigned', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='assigned_user', to=settings.AUTH_USER_MODEL)),
                ('fixed_versions', models.ManyToManyField(blank=True, related_name='fixed_version', to='main.Version')),
                ('reporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reporter_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]