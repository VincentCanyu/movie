# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-03-06 13:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20190306_2119'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.RemoveField(
            model_name='movie_detail',
            name='category',
        ),
        migrations.AddField(
            model_name='movie_detail',
            name='category',
            field=models.ManyToManyField(to='users.Category', verbose_name='类型'),
        ),
    ]
