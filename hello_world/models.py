from django.db import models

# Create your models here.
class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    likes = models.IntegerField()
    verified = models.BinaryField()
    added = models.DateTimeField()
    modified = models.DateTimeField()