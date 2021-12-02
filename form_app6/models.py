from django.db import models

# Create your models here.
class Task(models.Model):
    text = models.TextField()

    def __str__(self):
        return f"{self.text}"  # Pokazuje tekst (zadania) zamiast Tasks, tzn. pokazuje to co zostało wpisane
