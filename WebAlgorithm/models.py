from django.db import models
from django.contrib.auth.models import User
import django.utils.timezone as tm
import random
import os
from django.utils.text import slugify

def week_delta():
    return tm.now().date() + tm.timedelta(weeks=1)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True, verbose_name='Номер телефона')
    age = models.PositiveSmallIntegerField(blank=True, verbose_name='Возраст', default=1)
    user_img = models.ImageField(upload_to='user_img/', verbose_name='Фото', default='user_img/default_user.png')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_teacher = models.BooleanField(default=False, verbose_name='Учитель?')

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name


class Course(models.Model):
    name = models.CharField(max_length=70, verbose_name="Название курса")
    course_img = models.ImageField(upload_to='course_img/', verbose_name='Превью', default='course_img/default_course.jpg')
    course_description = models.TextField(max_length=250, verbose_name='Описание', blank=True)
    course_teacher = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Учитель')
    update_time = models.DateTimeField(auto_now=True)
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    url = models.SlugField(max_length=100, unique=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.url = slugify(self.name)
        super(Course, self).save(*args, **kwargs)


class CourseList(models.Model):
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_id.user.first_name + ' ' + self.course_id.name


class Lesson(models.Model):
    lesson_title = models.CharField(max_length=100, verbose_name='Тема урока')
    description = models.TextField(max_length=10000, verbose_name='Описание урока', blank=True)
    attached_files = models.FileField(upload_to='attached_files/', verbose_name='Прикрепленные файлы', blank=True)
    fk_course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Урок курса')
    url = models.SlugField(unique=True)
    is_hidden = models.BooleanField(default=False, verbose_name='Скрыть?')
    update_time = models.DateTimeField(auto_now=True, verbose_name='Последнее изменение')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    HomeTask_title = models.CharField(max_length=200, verbose_name='Тема домашнего задания', blank=True, default='New', null=True)
    HomeTask_description = models.TextField(max_length=100000, verbose_name='Описание задания', blank=True, default='New', null=True)
    deadline_time = models.DateField(verbose_name='Дата сдачи', default=week_delta)
    is_hometask = models.BooleanField(verbose_name='Не прекреплять домашнее задание', default=False)

    def __str__(self):
        return 'Курс:   ' + self.fk_course.name + '   <<I I>>   Урок:   ' + self.lesson_title

    def save(self, *args, **kwargs):
        self.url = slugify(self.lesson_title[0:15]+'-'+self.fk_course.name)
        super(Lesson, self).save(*args, **kwargs)

    def filename(self):
        return os.path.basename(self.attached_files.name)


class HomeTask(models.Model):
    fk_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='Д/з урока --')
    fk_user = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Для ученика --')
    HomeTask_attached_files = models.FileField(upload_to=f'home_task/', verbose_name='Прикрепленные файлы', blank=True)
    update_time = models.DateTimeField(auto_now=True, verbose_name='Последнее изменение')
    comment = models.TextField(max_length=100000, blank=True, verbose_name='Комментарий преподавателя')
    is_passed = models.BooleanField(default=False, verbose_name="Сдано?")
    mark = models.IntegerField(verbose_name='Оценка', choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'),
                                                               (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], blank=None, default=0)

    def __str__(self):
        return self.fk_lesson.HomeTask_title + ' -> ' + self.fk_lesson.lesson_title + ' -> ' + self.fk_user.user.first_name


class CommentHomeTask(models.Model):
    fk_user = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Кто отправил')
    fk_home_task = models.ForeignKey(HomeTask, on_delete=models.CASCADE, verbose_name='Чье дз')
    comment_text = models.TextField(max_length=1000, verbose_name='Текст комментрия')
    creation_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fk_user.user.first_name + self.fk_user.user.last_name + '--->>>' \
               + self.fk_home_task.fk_user.user.first_name + self.fk_home_task.fk_user.user.last_name
