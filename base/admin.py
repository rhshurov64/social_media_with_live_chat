from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id','user','bio','profileimg','location','created_at','updated_at','total_post', 'get_followers_count', 'get_following_count', 'get_blocklist']
    
    def get_followers_count(self, obj):
        return obj.followers.count()

    get_followers_count.short_description = 'Followers Count'

    def get_following_count(self, obj):
        return obj.following.count()

    get_following_count.short_description = 'Following Count'
    
    @admin.display(description='blocklist')
    def get_blocklist(self, obj):
        return [block.username for block in obj.blocklist.all()]
    
    
    
@admin.register(Verify_User)
class Verify_UserAdmin(admin.ModelAdmin):
    list_display = ['id','username','check_user','token']

    
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','author','authorprofile','username','text','postimg','created_at','updated_at','total_like','total_comment']
        
@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['id','user','post','created_at']
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id','author','post','text','created_at','updated_at']
    
@admin.register(Replay)
class ReplayAdmin(admin.ModelAdmin):
    list_display = ['id','author','post','comment', 'replay','created_at','updated_at']
    
@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    list_display = ['id','author','blocked_user','is_block']
    
@admin.register(UserLoginHistory)
class UserLoginHistoryAdmin(admin.ModelAdmin):
    list_display = ['user','login_time','logout_time', 'duration_minutes']
    
    
@admin.register(OnlineStatus)
class OnlineStatusAdmin(admin.ModelAdmin):
    list_display = ['user','status']



