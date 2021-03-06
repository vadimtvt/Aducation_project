# Generated by Django 3.1 on 2020-08-19 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebAlgorithm', '0016_lesson'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='url',
            field=models.SlugField(default='NONE', max_length=100, unique=True),
        ),
        migrations.AddField(
            model_name='lesson',
            name='url',
            field=models.SlugField(default=None, max_length=100, unique=True),
            preserve_default=False,
        ),
    ]
