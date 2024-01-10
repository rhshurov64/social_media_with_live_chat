from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='/login/')
def home(request):
    return render(request, 'video_conference/index.html')

@login_required(login_url='/login/')
def video_call(request):
    name = request.user.get_full_name
    return render(request, 'video_conference/video.html', {'name' : name})

@login_required(login_url='/login/')
def join(request):
    name = request.user.get_full_name
    if request.method == 'POST':
        roomID = request.POST['roomID']
        return redirect("/video_conference/video_call?roomID=" + roomID)
    return render(request, 'video_conference/join.html', {'name' : name})