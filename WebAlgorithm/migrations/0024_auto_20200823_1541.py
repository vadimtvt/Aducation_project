# Generated by Django 3.1 on 2020-08-23 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WebAlgorithm', '0023_lesson_is_hidden'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='is_hidden',
            field=models.BooleanField(default=False, verbose_name='Скрыть?'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='Последнее изменение'),
        ),
        migrations.CreateModel(
            name='HomeTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('HomeTask_title', models.CharField(max_length=200, verbose_name='Тема домашнего задания')),
                ('HomeTask_description', models.TextField(max_length=100000, verbose_name='Описание задания')),
                ('HomeTask_attached_files', models.FileField(blank=True, upload_to='home_task/<django.db.models.query_utils.DeferredAttribute object at 0x0421BE20>/<django.db.models.query_utils.DeferredAttribute object at 0x0420CC70>+"_"<django.db.models.query_utils.DeferredAttribute object at 0x0420CCA0>', verbose_name='Прикрепленные файлы')),
                ('fk_lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebAlgorithm.lesson', verbose_name='Д/з урока --')),
                ('fk_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebAlgorithm.profile', verbose_name='Для ученика --')),
            ],
        ),
    ]
