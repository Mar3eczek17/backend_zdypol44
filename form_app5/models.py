from django.db import models


# Create your models here.
class Task(models.Model):
    # db_table = ''
    text = models.TextField()

    def __str__(self):
        return f"{self.text}"
