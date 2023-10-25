from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id','user','bio','profileimg','location','created_at','updated_at','total_post', 'total_follower', 'total_following']
    
@admin.register(Verify_User)
class Verify_UserAdmin(admin.ModelAdmin):
    list_display = ['id','username','check_user','token']

    
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','author','authorprofile','username','text','postimg','created_at','updated_at','total_like','total_comment']
        
@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['id','username','post']
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id','author','post','text','created_at','updated_at']
