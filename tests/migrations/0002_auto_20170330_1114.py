# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-30 08:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='correctChoice',
            field=models.CharField(choices=[(models.CharField(max_length=128, verbose_name='а) :'), 'xxx'), ('б)', 'xxx'), ('в)', 'xxx'), ('г)', 'xxx')], max_length=128, verbose_name='Правильна відповідь:'),
        ),
    ]
