from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=128)
    capital = models.OneToOneField('Capital', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
# Create your models here.
class Capital(models.Model):
    name = models.CharField(max_length=128)  # ustawic unique=True w tej linijce i stworzymy tylko jedna Warszawe
    # country = models.OneToOneField()
    def __str__(self):
        return self.name

# class Country(models.Model):
#     name = models.CharField(max_length=128)
#     capital = models.OneToOneField(Capital, on_delete=models.CASCADE)


class Language(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Framework(models.Model):
    name = models.CharField(max_length=128)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Character(models.Model):
    name = models.CharField(max_length=128)
    movies = models.ManyToManyField(Movie)
    # comic = models.ManyToManyField() # trzeba stworzyc model comic


    def __str__(self):
        return self.name