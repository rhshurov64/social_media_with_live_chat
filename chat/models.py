from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    message = models.TextField()
    time= models.DateTimeField()
    group = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.sender} to {self.recipient} at {self.time}"
    

    
class Notification(models.Model):
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    like_notifcation = models.BooleanField(default=False)
    post_id = models.IntegerField(default=None, null=True)
    comment_id = models.IntegerField(default=None, null=True)
    comment_notifcation = models.BooleanField(default=False)
    replay_notifcation = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.receiver)
    