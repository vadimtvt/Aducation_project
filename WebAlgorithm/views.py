from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.views.generic import DetailView
from django.template.defaultfilters import date
import datetime
from .forms import *
from .models import *
from calendar import monthrange, weekday, month_name
from django.utils import dateformat
import os


class LoginPage(LoginView):
    template_name = 'login.html'
    form_class = LoginForm


@login_required
def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    if request.method == 'POST':
        form = PictureForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()

    args = {'user': user,
            'course_list': CourseList.objects.all(),
            'course': Course.objects.all(),
            'form_pic': PictureForm}
    return render(request, 'Profile.html', args)


@login_required
def view_calendar(request):
    user = request.user
    user_course_list = CourseList.objects.filter(user_id=user.profile)
    day_name = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
    days = monthrange(tm.now().year, tm.now().month)
    list_week_days = [(day_name[weekday(tm.now().year, tm.now().month, i)], i,
                       HomeTask.objects.filter(fk_user=user.profile,
                                               fk_lesson__deadline_time=datetime.datetime(tm.now().year, tm.now().month,
                                                                                          i)),
                       Lesson.objects.filter(deadline_time=datetime.datetime(tm.now().year, tm.now().month, i))) for i
                      in range(1, days[1] + 1)]
    if request.method == 'POST':
        form = PictureForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()

    args = {'user': user,
            'course_list': user_course_list,
            'course': Course.objects.all(),
            'form_pic': PictureForm,
            'number_days': range(1, days[1] + 1),
            'week_days': list_week_days,
            'month': date(datetime.date.today(), 'F'),
            'month_number': tm.now().month,
            'year': tm.now().year,
            'number_day_today': tm.now().day,
            }
    return render(request, 'Calendar.html', args)


@login_required
def view_course(request, slug=None):
    course = Course.objects.get(url=slug)
    lessons = Lesson.objects.all()
    args = {'course_cur': course,
            'lessons': lessons,
            'course_list': CourseList.objects.all(),
            'course': Course.objects.all(),
            'form_pic': PictureForm}
    return render(request, 'Course.html', args)


@login_required
def view_lesson(request, slug1=None, slug2=None):
    course = Course.objects.get(url=slug1)
    lesson = Lesson.objects.get(url=slug2)
    try:
        check_box = 1
        home_task = HomeTask.objects.get(fk_lesson=lesson, fk_user=request.user.profile)
    except:
        check_box = 0
        home_task = HomeTask.objects.create(fk_lesson=lesson, fk_user=request.user.profile)

    comments = CommentHomeTask.objects.filter(fk_home_task=home_task)
    if request.method == 'POST':
        form = HomeTaskForm(request.POST, request.FILES, instance=home_task)
        comment_form = CommentForm(request.POST, request.FILES)
        if form.is_valid() and comment_form.is_valid():
            form.save()
            comment_form.save()
            return redirect(f'../{course.url}/{lesson.url}#hometask')
        elif form.is_valid() and not comment_form.is_valid():
            form.save()
            return redirect(f'../{course.url}/{lesson.url}#hometask')
        elif not form.is_valid() and comment_form.is_valid():
            comment_form.save()
            return redirect(f'../{course.url}/{lesson.url}#comment')
    else:
        form = HomeTaskForm()
        if not check_box and not comments:
            home_task.delete()

    args = {'course_cur': course,
            'lesson': lesson,
            'course_list': CourseList.objects.all(),
            'course': Course.objects.all(),
            'form_pic': PictureForm,
            'home_task': home_task,
            'home_task_all': HomeTask.objects.all(),
            'home_task_form': HomeTaskForm(instance=home_task),
            'time_left': lesson.deadline_time - tm.now().date(),
            'time_now': tm.now(),
            'comments': comments,
            'comment_form': CommentForm(initial={'fk_home_task': home_task, 'fk_user': request.user.profile}),
            }
    return render(request, 'Lesson.html', args)


@login_required
def edit_teacher(request, slug1=None, slug2=None, slug3=None):
    course = Course.objects.get(url=slug1)
    lesson = Lesson.objects.get(url=slug2)
    errors = ''
    if request.method == 'POST':
        form = LessonTeacherForm(request.POST, request.FILES, instance=lesson)
        if form.is_valid():
            form.save()
            return redirect(f'../{lesson.url}')
        else:
            errors = form.errors

    args = {'course_cur': course,
            'lesson': lesson,
            'course_list': CourseList.objects.all(),
            'course': Course.objects.all(),
            'form_pic': PictureForm,
            'time_left': lesson.deadline_time - tm.now().date(),
            'time_now': tm.now(),
            'Lesson_form': LessonTeacherForm(instance=lesson, initial={
                'deadline_time': dateformat.format(lesson.deadline_time, 'Y-m-d')}),
            'errors': errors,
            }
    return render(request, 'Edit_Lesson.html', args)


@login_required
def add_lesson(request, slug1=None):
    course = Course.objects.get(url=slug1)
    errors = ''
    if request.method == 'POST':
        form = AddLessonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(f'../{course.url}')
        else:
            errors = form.errors

    args = {'course_cur': course,
            'course_list': CourseList.objects.all(),
            'course': Course.objects.all(),
            'form_pic': PictureForm,
            'time_now': tm.now(),
            'Lesson_form': AddLessonForm(initial={'url': course.name + str(random.randint(1, 1000)),
                                                  'fk_course': course,
                                                  'deadline_time': dateformat.format(
                                                      tm.now().date() + tm.timedelta(weeks=1), 'Y-m-d')
                                                  }),
            'errors': errors,
            }
    return render(request, 'Add_Lesson.html', args)


@login_required
def edit_teacher_course(request, slug1=None):
    course = Course.objects.get(url=slug1)
    errors = ''
    if request.method == 'POST':
        form = CourseFormEdit(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            return redirect(f'../{course.url}')
        else:
            errors = form.errors

    args = {'course_cur': course,
            'FormEdit': CourseFormEdit(instance=course),
            'course_list': CourseList.objects.all(),
            'course': Course.objects.all(),
            'form_pic': PictureForm,
            'errors': errors,
            }
    return render(request, 'Edit_Course.html', args)


@login_required
def view_home_task(request, slug1=None, slug2=None, pk=None):
    errors = ''
    course = Course.objects.get(url=slug1)
    lesson = Lesson.objects.get(url=slug2)
    owner_home_task = Profile.objects.get(pk=pk)
    current_home_task = HomeTask.objects.get(fk_lesson=lesson, fk_user=owner_home_task)
    comments = CommentHomeTask.objects.filter(fk_home_task=current_home_task)
    if request.method == 'POST':
        form = HomeTaskTeacherForm(request.POST, request.FILES, instance=current_home_task)
        comment_form = CommentForm(request.POST, request.FILES)

        if form.is_valid() and comment_form.is_valid():
            form.save()
            comment_form.save()
            return redirect(f'../{lesson.url}/{pk}#comment')
        elif form.is_valid() and not comment_form.is_valid():
            form.save()
            return redirect(f'../{lesson.url}/{pk}')
        elif not form.is_valid() and comment_form.is_valid():
            comment_form.save()
            return redirect(f'../{lesson.url}/{pk}#comment')
    else:
        if not current_home_task.HomeTask_attached_files and not comments:
            current_home_task.delete()

    args = {'course_cur': course,
            'FormEdit': CourseFormEdit(instance=course),
            'course_list': CourseList.objects.all(),
            'course': Course.objects.all(),
            'form_pic': PictureForm,
            'errors': errors,
            'comments': comments,
            'lesson': lesson,
            'cur_ht': current_home_task,
            'home_task_form': HomeTaskTeacherForm(instance=current_home_task),
            'comment_form': CommentForm(initial={'fk_home_task': current_home_task, 'fk_user': request.user.profile}),
            }
    return render(request, 'Check_HT.html', args)


def logout(request):
    auth.logout(request)
    return redirect('../../')


def del_comment(request, slug1=None, slug2=None, pk=None):
    comment = CommentHomeTask.objects.get(pk=pk)
    course = Course.objects.get(url=slug1)
    if request.user.id == comment.fk_user.user.id or course.course_teacher.user.id == request.user.id:
        comment.delete()
    lesson_url = comment.fk_home_task.fk_lesson.url
    if course.course_teacher.user.id == request.user.id:
        return redirect(f'../../{lesson_url}/{comment.fk_home_task.fk_user.id}#comment')
    else:
        return redirect(f'../../{lesson_url}#comment')
