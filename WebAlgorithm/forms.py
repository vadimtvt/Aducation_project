from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import *


class LoginForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control mt-2'


class PictureForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('user_img',)
        help_texts = ''

    def __init__(self, *args, **kwargs):
        super(PictureForm, self).__init__(*args, **kwargs)
        self.fields['user_img'].label = ""
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control-file form_pic custom-file-input'
            visible.field.widget.attrs["onchange"] = "form.submit()"


class HomeTaskForm(forms.ModelForm):
    class Meta:
        model = HomeTask
        fields = ('HomeTask_attached_files',)

    def __init__(self, *args, **kwargs):
        super(HomeTaskForm, self).__init__(*args, **kwargs)
        self.fields['HomeTask_attached_files'].label = ""
        # self.fields['HomeTask_attached_files'].widget.attrs.update({'class': 'custom-file-input'})


class LessonTeacherForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ('lesson_title', 'description', 'attached_files',
                  'url', 'is_hidden', 'HomeTask_title', 'HomeTask_description',
                  'deadline_time', 'is_hometask',)
        widgets = {
            'deadline_time': forms.DateInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super(LessonTeacherForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.fields['is_hidden'].widget.attrs.update({'class': 'custom-control-input'})
        self.fields['is_hometask'].widget.attrs.update({'class': 'custom-control-input'})
        self.fields['attached_files'].widget.attrs.update({'class': 'file_class form-control'})


class AddLessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ('lesson_title', 'description', 'attached_files',
                  'url', 'is_hidden', 'HomeTask_title', 'HomeTask_description',
                  'deadline_time', 'fk_course', 'is_hometask',)

        widgets = {
            'deadline_time': forms.DateInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super(AddLessonForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.fields['is_hidden'].widget.attrs.update({'class': 'custom-control-input'})
        self.fields['is_hometask'].widget.attrs.update({'class': 'custom-control-input'})
        self.fields['attached_files'].widget.attrs.update({'class': 'file_class form-control'})


class HomeTaskTeacherForm(forms.ModelForm):
    class Meta:
        model = HomeTask
        fields = ('HomeTask_attached_files', 'comment', 'is_passed', 'mark')

    def __init__(self, *args, **kwargs):
        super(HomeTaskTeacherForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            self.fields['is_passed'].widget.attrs.update({'class': 'custom-control-input'})


class CourseFormEdit(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('name', 'course_img', 'course_description', )

    def __init__(self, *args, **kwargs):
        super(CourseFormEdit, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            self.fields['course_img'].widget.attrs.update({'class': 'file_class form-control'})


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentHomeTask
        fields = ('fk_user', 'fk_home_task', 'comment_text')

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['comment_text'].widget.attrs.update({'placeholder': 'Ваш комментарий ...'})
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control text_form_'