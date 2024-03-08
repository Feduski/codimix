from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('process_user_input/', views.process_user_input, name='process_user_input'),
]