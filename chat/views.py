from django.shortcuts import render
from base.models import *
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    user = request.user
    alluser = User.objects.all()
    alluserprofile = Profile.objects.all()
    userdetails = User.objects.exclude(username = user)
    userprofile = Profile.objects.exclude(user = user)
    return render(request, 'chat/index.html', {'alluser': alluser, 'alluserprofile': alluserprofile ,'userdetails': userdetails, 'userprofile': userprofile})