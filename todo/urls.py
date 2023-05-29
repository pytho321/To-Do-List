from django.contrib import admin
from django.urls import path
from mainapp import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('tasks/create/', views.create_task, name='create_task'),
    path('delete/<str:task_id>/', views.delete, name='delete')
]
