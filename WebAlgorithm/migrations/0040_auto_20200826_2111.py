# Generated by Django 3.1 on 2020-08-26 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebAlgorithm', '0039_auto_20200826_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='url',
            field=models.SlugField(unique=True),
        ),
    ]
