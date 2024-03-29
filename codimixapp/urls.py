from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('base/', views.base, name='base'),
    path('process_user_input/', views.process_user_input, name='process_user_input'),
    path('register/', views.register_view, name='register'),
]