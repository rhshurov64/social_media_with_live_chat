from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.contrib.auth.models import User
import json
import datetime
from .models import *



class ChatConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        user_id = self.scope['user'].id
        
        other_username = self.scope['url_route']['kwargs']['username']
        other_user = await self.get_user(other_username)
        
        other_user_id = other_user.id
        
        sorted_id = sorted([user_id, other_user_id])
        self.group_name = f"chat_{sorted_id[0]}_{sorted_id[1]}"
        
        print(self.group_name)
        
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        
        await self.accept()
        
    async def receive(self, text_data=None, bytes_data=None):
        print("recived")
        
        current_datetime = datetime.datetime.now()
        formatted_time = current_datetime.strftime('%b. %d, %Y, %I:%M %p')
        formatted_time = formatted_time[:-2] + formatted_time[-2].lower() + '.' + formatted_time[-1].lower() + '.'
        
        data = json.loads(text_data)
        message = data['msg']
        print(message)
        
        sender = self.scope['user']
        username = self.scope['url_route']['kwargs']['username']
        receiver = await self.get_user(username)
        
        await self.save_messaage(sender, receiver, message, current_datetime, self.group_name)
        
        
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'chat.message',
                'message': message,
                'sender' : str(sender),
                'time': formatted_time
            }
        )
        
        
        
    async def chat_message(self, event):
        sender_username = event['sender']
        message = event['message']
        time = event['time']
        
        await self.send(text_data=json.dumps({
            'msg': message,
            'sender': sender_username,
            'time' : time
            
        }))
        recipient_username = self.scope['url_route']['kwargs']['username']
        recipient = await self.get_user(recipient_username)
        sender = await self.get_user(sender_username)
        await self.create_notification(recipient, sender, f'New message from {sender_username}', time)
        
        
        
    async def disconnect(self, close_code):
        print('Disconnect')
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )
        
    @database_sync_to_async
    def get_user(self, other_username):
        return User.objects.get(username = other_username)
    
    @database_sync_to_async
    def save_messaage(self, sender, receiver, message, time, group):
        msg = Message.objects.create(sender =sender, recipient =receiver, message =message, time = time, group= group)
        
        
    @database_sync_to_async
    def create_notification(self, receiver, sender, message, time):
        Notification.objects.create(receiver=receiver, sender =sender, message=message, timestamp=time)