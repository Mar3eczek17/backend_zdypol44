from django.db import models

# Create your models here.
class Message(models.Model):
    CHOICES = [
        ("question", "Pytanie"),
        ("other", "Inne")
    ]


    name = models.CharField(max_length=128)
    email = models.EmailField()
    category = models.CharField(max_length=16, choices=CHOICES)
    subject = models.CharField(max_length=128)
    body = models.TextField()
    date = models.DateField()
    time = models.TextField()
    added = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)