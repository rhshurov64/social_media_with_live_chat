from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'video_conference'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('video_call/', views.video_call, name='video_call'),
    path('join/', views.join, name='join'),
]