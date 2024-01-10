from django import forms
from .models import *
from django.contrib.auth.models import User
from django.forms import ClearableFileInput
from django.forms import inlineformset_factory



class UserDataForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name',)
        
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user','user.first_name','created_at','updated_at','total_like','total_comment','total_following', 'total_follower', 'total_post', 'followers', 'following', 'blocklist')
        # fields = ('user.first_name','bio', 'about', 'profileimg', 'location', 'country', 'facebook', 'twitter', 'linkdin', 'github',)
        # fields = '__all__'
        
        
class ProfileImageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profileimg',)
        
        
# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ('text',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
       
        
        
class ReplayForm(forms.ModelForm):
    class Meta:
        model = Replay
        fields = ('replay',)
        
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text']

ImageFormSet = inlineformset_factory(Post, Image, form=PostForm, fields=['image'], extra=0, can_delete=True)