# Generated by Django 3.1 on 2020-08-18 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WebAlgorithm', '0006_auto_20200818_1952'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebAlgorithm.course')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebAlgorithm.profile')),
            ],
        ),
    ]
