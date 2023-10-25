from django.shortcuts import render, redirect , HttpResponseRedirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from .models import *
from itertools import chain
import random
import uuid
from django.core.mail import send_mail
from django.conf import settings
from .forms import *
from django.db.models import Q

# Create your views here.

@login_required(login_url='/login/')
def index(request):
    data = User.objects.exclude(username = request.user).exclude(username = 'admin')
    status = Post.objects.all().order_by('-updated_at')
    
    user = request.user
    
    post = Post.objects.filter(username = user)
    total_post = len(post)
    
    comments = Comment.objects.all()
    
    
    
    if request.method == "POST":
        user = request.user
        author = User.objects.get(username = user)
        authorprofile = Profile.objects.get(user = user)
        text = request.POST['text']
        postimg = request.FILES.get('image', None)
        post = Post.objects.create(author = author, authorprofile = authorprofile, username = user, text=text, postimg = postimg)
        
    return render(request,'base/home.html', {'data':data, 'posts':status, 'total_post':total_post, 'comments': comments})



def rendertosetting(request):
    return render(request,'base/render.html')



def user_logout(request):
    logout(request)
    return redirect('login')



def login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            un = request.POST['username']
            pw = request.POST['password']
            userr = auth.authenticate(username=un, password=pw)
            
            if userr is not None:
                if userr.is_staff == True:
                    auth.login(request, userr)
                    return redirect('index')
                else:
                    checkk = Verify_User.objects.get(username = un)
                    if checkk.check_user == True:
                        auth.login(request, userr)
                        return redirect('index')
                    else:
                        messages.warning(request,"Please Verify Your Account First!")
            else:
                messages.info(request, 'Credentials Invalid')
                return redirect('login')
    else:
        return redirect('index')
    return render(request,'base/login.html')


@login_required(login_url='/login/')
def like(request):
    username = request.user.username
    
    post_id = request.GET.get('post_id')

    post = Post.objects.get(id=post_id)

    like_filter = Like.objects.filter(post_id=post_id, username=username).first()
    liked = Like.objects.filter(Q(post=post_id ) & Q(liked_status = True)).first()
    if like_filter == None:
        new_like = Like.objects.create(post_id=post_id, username=username)
        new_like.liked_status = True
        new_like.save()
        post.total_like = post.total_like+1
        post.save()
        return redirect('/', {'liked':liked})
    else:
        like_filter.delete()
        like_filter.like_status = False
        post.total_like = post.total_like-1
        post.save()
        return redirect('/')


@login_required(login_url='/login/')
def postdelete(request):
    post_id = request.GET.get('post_id')
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('/')

@login_required(login_url='/login/')
def comment_delete(request):
    cmnt_id = request.GET.get('cmnt_id')
    cmnt = Comment.objects.get(id = cmnt_id)
    cmnt.delete()
    return redirect('/')


@login_required(login_url='/login/')
def replay_delete(request):
    replay_id = request.GET.get('replay_id')
    replay = Replay.objects.get(id = replay_id)
    replay.delete()
    return redirect('/')


@login_required(login_url='/login/')
def profile_post_delete(request):
    post_id = request.GET.get('post_id')
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('/profile/')



def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password1']
        password2 = request.POST['password2']

        if password == password2:
            # if User.objects.filter(email=email).exists():
            #     messages.info(request, 'Email Taken')
            #     return redirect('signup')
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name )
                # user.save()
                
               
                
                u_id = str(uuid.uuid4())
                pro_obj = Verify_User.objects.create(user = user, username=username, token = u_id)
                sendemail(email, u_id)
                messages.success(request,'Registration Success, Verification link send in your email. Please Verify Your account!')
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)
                return redirect('signup') 
                
        else:
            messages.info(request, 'Password Not Matching')
            return redirect('signup')
        
    else:
        return render(request, 'base/signUp.html')

    
def sendemail(email,token):
    subject = 'Verify Email'
    message = f'Click on the link to verify your Account - http://127.0.0.1:8000/verify/{token}'
    print(message)
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject=subject,message=message,from_email=from_email,recipient_list=recipient_list)
    
    
def account_verify(request,token):
    pf = Verify_User.objects.filter(token = token).first()
    pf.check_user = True
    pf.save()
    messages.success(request,'Your Account is verifed, Please Complete your Profile!')
    return render(request, 'base/render.html')



    
@login_required(login_url='/login/')
def setting(request):
    if request.method == 'POST':
        user = request.user
        # print(user)
        userr = User.objects.get(username = user)
        image = request.FILES['image']
        bio = request.POST['bio']
        about = request.POST['about']
        location = request.POST['location']
        country = request.POST['country']
        facebook = request.POST['facebook']
        twitter = request.POST['twitter']
        linkdin = request.POST['linkdin']
        github = request.POST['github']
        new_profile = Profile.objects.create(user=userr, bio = bio, about = about, profileimg = image, location = location, country = country, facebook = facebook, twitter = twitter, linkdin = linkdin, github = github)
        new_profile.save()
        # new_profile = Profile.objects.filter(pk = userr.pk).update(bio = bio, profileimg = image, location = location)
        return redirect('index')
    return render(request, 'base/setting.html')


@login_required(login_url='/login/')
def profile(request, id):
    user_data = User.objects.get(id = id)
    profile_data = Profile.objects.get(user = user_data)
    posts = Post.objects.filter(author = user_data)
    post_length = len(posts)
    
    
    
    context = {
        "udata" : user_data,
        "profile_data" : profile_data,
        'posts' : posts,
        'post_length' : post_length,
    }


    
    return render(request,'base/profile.html',context)


@login_required(login_url='/login/')
def suggestion(request):
    data = User.objects.exclude(username = request.user).exclude(username = 'admin')
    return render(request,'base/suggestion.html',{'data':data})


@login_required(login_url='/login/')
def update(request,id):
    if request.method =='POST':
        pi = Profile.objects.get(pk= id)
        fm = ProfileForm(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Profile.objects.get(pk= id)
        fm = ProfileForm(instance=pi)
        
    return render(request,'base/update.html',{'form':fm})


@login_required(login_url='/login/')
def postedit(request, id):
    if request.method =='POST':
        pi = Post.objects.get(pk= id)
        fm = PostForm(request.POST, request.FILES, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Post.objects.get(pk= id)
        fm = PostForm(instance=pi)
    return render(request,'base/postedit.html',{'form':fm})



@login_required(login_url='/login/')
def commentedit(request, id):
    if request.method =='POST':
        pi = Comment.objects.get(pk= id)
        fm = CommentForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Comment.objects.get(pk= id)
        fm = CommentForm(instance=pi)
    return render(request,'base/commentedit.html',{'form':fm})


@login_required(login_url='/login/')
def replayedit(request, id):
    if request.method =='POST':
        pi = Replay.objects.get(pk= id)
        fm = ReplayForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Replay.objects.get(pk= id)
        fm = ReplayForm(instance=pi)
    return render(request,'base/replayedit.html',{'form':fm})







@login_required(login_url='/login/')
def comment(request, id):
    if request.method == 'POST':
        text = request.POST['comment']
        user = request.user
        author = User.objects.get(username = user)
        authorprofile = Profile.objects.get(user = user)
        post_obj = Post.objects.get(id = id)
        comment = Comment.objects.create(author= author, authorprofile =authorprofile, post = post_obj, text = text)
        if comment:
            post_obj.total_comment= post_obj.total_comment + 1
            post_obj.save()
    return HttpResponseRedirect(f'show_comment/{id}')


@login_required(login_url='/login/')
def show_comment(request, id):
    post = Post.objects.filter(id = id).order_by('-created_at')
    comments = Comment.objects.filter(post__in= post).order_by('-created_at')
    return render(request, 'base/comment.html', {'posts':post, 'comments': comments})



@login_required(login_url='/login/')
def show_replay(request, pid, cid):
    
    post = Post.objects.filter(id = pid)
    comments = Comment.objects.filter(id= cid)
    replays = Replay.objects.filter(comment__in = comments)
    
    if request.method == 'POST':
        replay = request.POST['replay']
        user = request.user
        author = User.objects.get(username = user)
        authorprofile = Profile.objects.get(user = user)
        posts = Post.objects.get(id = pid)
        cmnt = Comment.objects.get(id = cid)
        replay = Replay.objects.create(author= author, authorprofile =authorprofile,post = posts, comment = cmnt, replay = replay)
        if replay:
            posts.total_comment= posts.total_comment + 1
            posts.save()
    
    return render(request, 'base/replay.html', {'posts':post, 'comments': comments, 'replays':replays})
    

def newprofile(request, id):
    user_data = User.objects.get(id = id)
    profile_data = Profile.objects.get(user = user_data)
    posts = Post.objects.filter(author = user_data)
    post_length = len(posts)
    
    
    
    context = {
        "udata" : user_data,
        "profile_data" : profile_data,
        'posts' : posts,
        'post_length' : post_length,
    }


    
    return render(request,'base/newprofile.html',context)