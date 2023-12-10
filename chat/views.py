from django.shortcuts import render, redirect
from base.models import *
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    user = request.user
    alluser = User.objects.all()
    alluserprofile = Profile.objects.all()
    userdetails = User.objects.exclude(username = user)
    userprofile = Profile.objects.exclude(user = user)
    return render(request, 'chat/index.html', {'alluser': alluser, 'alluserprofile': alluserprofile ,'userdetails': userdetails, 'userprofile': userprofile})


def chat_profile(request, username):
    user = request.user
    alluser = User.objects.all()
    alluserprofile = Profile.objects.all()
    userdetails = User.objects.exclude(username = user)
    userprofile = Profile.objects.exclude(user = user)
    
    
    chatbox_user= User.objects.get(username = username)
    chatbox_profile = Profile.objects.get(user = chatbox_user)
    
    status_user = OnlineStatus.objects.get(user = chatbox_user)
    
    user_id = user.id
    other_user = User.objects.get(username= username)
    
    messages = Message.objects.filter(
        group__in=[f"chat_{request.user.id}_{other_user.id}", f"chat_{other_user.id}_{request.user.id}"]
    ).order_by('time')
    
    
    return render(request, 'chat/chatpage.html', {'alluser': alluser, 'alluserprofile': alluserprofile ,'userdetails': userdetails, 'userprofile': userprofile, 'chatbox_profile':chatbox_profile, 'username':username, 'messages':messages, 'status_user':status_user})



def notification(request):
    user_notifications = Notification.objects.filter(receiver=request.user).order_by('-timestamp')
    
    # Update is_read for all notifications
    user_notifications.update(is_read=True)
    
    
    
    
   
    return render(request, 'chat/notification.html', {'user_notifications':user_notifications})

def notification_delete(request, id):
    notification = Notification.objects.get(id=id)
    notification.delete()
    return redirect('chat:notification')



def custom_processor(request):
    if request.user.is_authenticated:
        notification_count = Notification.objects.filter(receiver=request.user, is_read= False).count()
    else:
        notification_count = 0
    return {"notification_count": notification_count}