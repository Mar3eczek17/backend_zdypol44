from django.db import models
from django.shortcuts import reverse

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=64)
    age = models.IntegerField()
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name} z {self.city} <{self.age}>"

    def get_absolute_url(self):
        return reverse('viewapp:create-person3')