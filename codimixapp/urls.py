from django.contrib import admin
from codimixapp import views
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', views.home, name='home'),
    path('base/', views.base, name='base'),
    path('process_user_input/', views.process_user_input, name='process_user_input'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name='login'),
    path('testing/', views.testing_files, name='testing')
]