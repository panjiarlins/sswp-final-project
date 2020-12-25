from django.urls import path, include
from . import views
from .controller import registration_controller

urlpatterns = [
    path('', views.index, name='index'),
    path('covid_info/', views.covid_info, name='covid_info'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', registration_controller.index, name='register'),

    path('subject/', views.subject_list, name='subject'),
    path('subject/add/', views.subject_add, name='subject_add'),
    path('subject/edit/<int:subject_id>/', views.subject_edit, name='subject_edit'),
    path('subject/delete/<int:subject_id>/', views.subject_delete, name='subject_delete'),

    path('employee/', views.employee_list, name='employee'),
    path('employee/add/', views.employee_add, name='employee_add'),
    path('employee/edit/<int:employee_id>/', views.employee_edit, name='employee_edit'),
    path('employee/delete/<int:employee_id>/', views.employee_delete, name='employee_delete'),

    path('student/', views.student_list, name='student'),
    path('student/add/', views.student_add, name='student_add'),
    path('student/edit/<int:student_id>/', views.student_edit, name='student_edit'),
    path('student/delete/<int:student_id>/', views.student_delete, name='student_delete'),
]