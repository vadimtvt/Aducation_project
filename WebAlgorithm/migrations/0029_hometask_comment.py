# Generated by Django 3.1 on 2020-08-25 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebAlgorithm', '0028_auto_20200825_1851'),
    ]

    operations = [
        migrations.AddField(
            model_name='hometask',
            name='comment',
            field=models.TextField(blank=True, max_length=100000, verbose_name='Комментарий преподавателя'),
        ),
    ]
