from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.index, name='chat_index')
]
