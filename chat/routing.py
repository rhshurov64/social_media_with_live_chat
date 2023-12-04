from django.urls import path
from . import consumers


websocket_urlpatterns =[
    # path('ws/sc/<str:groupname>/', consumers.MySync.as_asgi()),
    path('chat/<str:username>/', consumers.ChatConsumer.as_asgi()),
]