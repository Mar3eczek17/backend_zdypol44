from django.db import models

# Create your models here.
class Message(models.Model):
    title = models.CharField(max_length=128)
    email = models.EmailField()
    body = models.TextField()