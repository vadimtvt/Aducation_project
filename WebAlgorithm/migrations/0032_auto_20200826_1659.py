# Generated by Django 3.1 on 2020-08-26 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebAlgorithm', '0031_auto_20200826_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='HomeTask_description',
            field=models.TextField(blank=True, max_length=100000, verbose_name='Описание задания'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='HomeTask_title',
            field=models.CharField(blank=True, max_length=200, verbose_name='Тема домашнего задания'),
        ),
    ]
