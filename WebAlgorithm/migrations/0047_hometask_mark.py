# Generated by Django 3.1 on 2020-10-14 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebAlgorithm', '0046_auto_20200901_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='hometask',
            name='mark',
            field=models.IntegerField(blank=None, choices=[(1, 'один'), (2, 'два'), (3, 'три')], default=0, verbose_name='Оценка'),
        ),
    ]
