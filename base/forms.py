from django import forms
from .models import *


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user','profileimg',)
        # fields = '__all__'
        
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text', 'postimg')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
       
        
        
class ReplayForm(forms.ModelForm):
    class Meta:
        model = Replay
        fields = ('replay',)
        
        
