# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-06 11:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='photos/')),
                ('name', models.CharField(max_length=30)),
                ('descripton', models.TextField()),
                ('time_uloaded', models.DateTimeField(auto_now_add=True, null=True)),
                ('category', models.ManyToManyField(to='pictures.categories')),
                ('location_taken', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pictures.Location')),
            ],
        ),
    ]
