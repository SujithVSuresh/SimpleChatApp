from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    date_created = models.DateTimeField(default=timezone.now) 
    created_by = models.ForeignKey(User, default="", null="True", blank="True", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Messages(models.Model):
    value = models.CharField(max_length=200)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    message_created_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.value    

