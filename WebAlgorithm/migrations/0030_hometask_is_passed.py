# Generated by Django 3.1 on 2020-08-25 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebAlgorithm', '0029_hometask_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='hometask',
            name='is_passed',
            field=models.BooleanField(default=False, verbose_name='Сдано?'),
        ),
    ]