# Generated by Django 3.1 on 2020-08-19 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WebAlgorithm', '0019_auto_20200819_2122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='url',
        ),
    ]
