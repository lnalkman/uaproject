# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-30 08:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correctChoice', models.CharField(choices=[('а)', 'xxx'), ('б)', 'xxx'), ('в)', 'xxx'), ('г)', 'xxx')], max_length=128, verbose_name='Правильна відповідь:')),
                ('first', models.CharField(max_length=128, verbose_name='а) :')),
                ('second', models.CharField(max_length=128, verbose_name='б) :')),
                ('third', models.CharField(max_length=128, verbose_name='в) :')),
                ('fourth', models.CharField(max_length=128, verbose_name='г) :')),
            ],
        ),
    ]
