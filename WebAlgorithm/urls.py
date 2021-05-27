from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import *

urlpatterns = [
    path('', LoginPage.as_view()),
    path('accounts/login/', LoginPage.as_view()),
    path('accounts/profile/', view_profile),
    path('accounts/profile/calendar', view_calendar),
    path('course/<slug:slug1>/<slug:slug2>/DelComment/<int:pk>', del_comment),
    path('accounts/logout/', logout),
    path('course/<slug:slug>/', view_course),
    path('course/<slug:slug1>/EditPage', edit_teacher_course),
    path('course/<slug:slug1>/AddLesson', add_lesson),
    path('course/<slug:slug1>/<slug:slug2>', view_lesson),
    path('course/<slug:slug1>/<slug:slug2>/<int:pk>', view_home_task),

    path('course/<slug:slug1>/<slug:slug2>/EditPage', edit_teacher),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

