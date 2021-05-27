# Generated by Django 3.1 on 2020-08-26 14:09

import WebAlgorithm.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebAlgorithm', '0036_auto_20200826_1707'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='HomeTask_description',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='HomeTask_title',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='deadline_time',
        ),
        migrations.AddField(
            model_name='hometask',
            name='HomeTask_description',
            field=models.TextField(blank=True, default='New', max_length=100000, null=True, verbose_name='Описание задания'),
        ),
        migrations.AddField(
            model_name='hometask',
            name='HomeTask_title',
            field=models.CharField(blank=True, default='New', max_length=200, null=True, verbose_name='Тема домашнего задания'),
        ),
        migrations.AddField(
            model_name='hometask',
            name='deadline_time',
            field=models.DateTimeField(default=WebAlgorithm.models.week_delta, verbose_name='Дата сдачи'),
        ),
    ]
