from django.urls import path, include
from . import views
from .controller import registration_controller
from .controller import subject_controller
from .controller import employee_controller
from .controller import student_controller

urlpatterns = [
    path('', views.index, name='index'),
    path('covid_info/', views.covid_info, name='covid_info'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', registration_controller.index, name='register'),

    path('subject/', subject_controller.subject_list, name='subject'),
    path('subject/add/', subject_controller.subject_add, name='subject_add'),
    path('subject/edit/<int:subject_id>/', subject_controller.subject_edit, name='subject_edit'),
    path('subject/delete/<int:subject_id>/', subject_controller.subject_delete, name='subject_delete'),

    path('employee/', employee_controller.employee_list, name='employee'),
    path('employee/add/', employee_controller.employee_add, name='employee_add'),
    path('employee/edit/<int:employee_id>/', employee_controller.employee_edit, name='employee_edit'),
    path('employee/delete/<int:employee_id>/', employee_controller.employee_delete, name='employee_delete'),

    path('student/', student_controller.student_list, name='student'),
    path('student/add/', student_controller.student_add, name='student_add'),
    path('student/edit/<int:student_id>/', student_controller.student_edit, name='student_edit'),
    path('student/delete/<int:student_id>/', student_controller.student_delete, name='student_delete'),
]