from django.contrib import admin
from .models import *
# Register your models here.

    

    
    
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['id','sender', 'recipient', 'message', 'time', 'group']
    
@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['id','sender','receiver', 'message', 'timestamp', 'is_read', 'like_notifcation','follow_notifcation', 'comment_notifcation','replay_notifcation', 'post_id', 'comment_id']