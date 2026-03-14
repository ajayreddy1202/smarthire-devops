# tracker/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('jobs/', views.job_list, name='job_list'),
    path('jobs/add/', views.add_job, name='add_job'),
    path('jobs/edit/<int:pk>/', views.edit_job, name='edit_job'),
    path('jobs/delete/<int:pk>/', views.delete_job, name='delete_job'),
]