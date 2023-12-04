from django.contrib import admin
from .models import *
# Register your models here.

    

    
    
@admin.register(Message)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['id','sender', 'recipient', 'message', 'time', 'group']