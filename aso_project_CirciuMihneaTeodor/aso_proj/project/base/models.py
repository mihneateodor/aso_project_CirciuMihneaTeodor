from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Room(models.Model):
    host = models.ForeignKey(User, on_delete= models.SET_NULL, null=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    participants = models.ManyToManyField(User, related_name='participants', blank=True)

    def __str__(self):
        return self.name

class Message(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    room = models.ForeignKey(Room, on_delete= models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]