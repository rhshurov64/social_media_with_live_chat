from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.index, name='chat_index'),
    path('msg/<str:username>/', views.chat_profile , name='chat_profile'),
    path('notification/', views.notification , name='notification'),
    path('notification_delete/<str:id>/', views.notification_delete , name='notification_delete'),
]
