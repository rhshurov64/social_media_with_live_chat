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
    

    