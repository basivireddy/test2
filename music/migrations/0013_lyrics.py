# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-04-19 10:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0012_auto_20170101_0528'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lyrics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=20)),
                ('lyric', models.TextField(max_length=1000)),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.Song')),
            ],
        ),
    ]
