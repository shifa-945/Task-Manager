from django.contrib import admin
from django.urls import path

from Taskapp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('login/',views.User_login,name='login'),
    path('after_login/',views.after_login,name='after_login'),
    path('logout/',views.User_logout,name='logout'),
    path('Task_add/', views.Task_add, name='Task_add'),
    path('Task_list/', views.Task_list, name='Task_list'),
    path('toggle/<int:id>/',views.toggle_task,name='toggle'),
    path('Task_delete/<int:id>/', views.Task_delete, name='Task_delete')
]
