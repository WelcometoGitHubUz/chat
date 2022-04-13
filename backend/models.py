from email.mime import audio
from django.db import models

class Post(models.Model):
    nomi = models.CharField(max_length=100)
    rasm = models.ImageField()
    def __str__(self):
        return self.nomi



class Messages(models.Model):
    message = models.TextField()
    img = models.ImageField()
    isRead = models.BooleanField(default=False)
    sendTime = models.DateTimeField(auto_now_add=True, blank=True)
    def __str__(self):
        return self.message