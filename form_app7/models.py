from django.db import models

# Create your models here.
class Message(models.Model):
    title = models.CharField(max_length=128)
    email = models.EmailField()
    body = models.TextField()
    category = models.CharField(max_length=128, null=True)
    added = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    date = models.DateTimeField()