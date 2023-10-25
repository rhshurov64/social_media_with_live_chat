from django.shortcuts import render, redirect

# Create your views here.

def home(request):
    return render(request, 'video_conference/index.html')


def video_call(request):
    name = request.user.get_full_name
    return render(request, 'video_conference/video.html', {'name' : name})

def join(request):
    name = request.user.get_full_name
    if request.method == 'POST':
        roomID = request.POST['roomID']
        return redirect("/video_conference/video_call?roomID=" + roomID)
    return render(request, 'video_conference/join.html', {'name' : name})