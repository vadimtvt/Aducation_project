# Generated by Django 3.1 on 2020-08-23 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebAlgorithm', '0024_auto_20200823_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hometask',
            name='HomeTask_attached_files',
            field=models.FileField(blank=True, upload_to='home_task/<django.db.models.query_utils.DeferredAttribute object at 0x03B1BE20>/<django.db.models.fields.related_descriptors.ForwardOneToOneDescriptor object at 0x03B1B4D8>', verbose_name='Прикрепленные файлы'),
        ),
    ]