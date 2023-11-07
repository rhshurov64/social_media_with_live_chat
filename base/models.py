from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,  null=True, blank=True)
    bio = models.CharField(null=True, blank=True, max_length= 121)
    about = models.TextField(null=True, blank=True)
    profileimg = models.ImageField(upload_to='profile/', default='blank-profile-picture.png', max_length=250)
    location = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100,  null=True, blank=True)
    facebook =models.URLField(max_length=200, null=True, blank=True)
    twitter =models.URLField(max_length=200, null=True, blank=True)
    linkdin = models.URLField(max_length=200, null=True, blank=True)
    github = models.URLField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    total_post = models.IntegerField(default=0)
    total_follower = models.IntegerField(default=0)
    total_following = models.IntegerField(default=0)
    
    

    def __str__(self):
        return self.user.username
    
class Verify_User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(max_length=100)
    token = models.CharField(max_length=100)
    check_user = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username
    


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    authorprofile = models.ForeignKey(Profile, on_delete=models.CASCADE,  null=True, blank=True)
    username = models.CharField(max_length=100)
    text = models.CharField(max_length=500, null=True, blank= True)
    postimg = models.ImageField(upload_to='post/', max_length=250, null=True, blank= True, default = None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    total_like = models.IntegerField(default=0)
    total_comment = models.IntegerField(default=0)
    
    
    def __str__(self):
        return str(self.id)
    
class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(max_length=100, default=None)
    liked_status = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username
    
    
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    authorprofile = models.ForeignKey(Profile, on_delete=models.CASCADE,  null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    text = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    
    def __str__(self):
        return str(self.id)
    
    
class Replay(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    authorprofile = models.ForeignKey(Profile, on_delete=models.CASCADE,  null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, blank=True)
    replay = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.id)
    
    

class Follow(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE, related_name="following")
    user_id_profile = models.ForeignKey(Profile,on_delete=models.CASCADE, related_name="following_profile")
    following_user = models.ForeignKey(User,on_delete=models.CASCADE, related_name="followers")
    following_user_profile = models.ForeignKey(Profile,on_delete=models.CASCADE, related_name="followers_profile")
    created = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return str(f"{self.user_id} follows {self.following_user}")
        
        
class Block(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE, related_name="user")
    authorprofile = models.ForeignKey(Profile,on_delete=models.CASCADE, default=None, related_name="authorprofile")
    blocked_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blocked_user")
    blocked_user_profile = models.ForeignKey(Profile,on_delete=models.CASCADE, default=None, related_name="blocked_user_profile")
    is_block = models.BooleanField(default=False)
    
    def __str__(self):
       return str(f"{self.author} blocked {self.blocked_user}")