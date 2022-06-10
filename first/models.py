from unicodedata import name
from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class Movie(models.Model):
    imdb_title_id = models.CharField(max_length=128, blank=False, null=False)
    original_title = models.CharField(max_length=128, blank=False, null=False)
    year = models.IntegerField()
    genre = models.CharField(max_length=128, blank=False, null=False)
    duration = models.IntegerField()
    director = models.CharField(max_length=128, blank=False, null=False)
    writer = models.CharField(max_length=128, blank=False, null=False)
    production_company = models.CharField(max_length=128, blank=False, null=False)
    actors = models.CharField(max_length=128, blank=False, null=False)
    description = models.TextField()
    avg_vote = models.FloatField()
    votes = models.IntegerField()

    def __str__(self):
        return f'{self.original_title}'


# One to Many

class Author(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)


class Article(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


# One to One 

# class Engine(models.Model):
#     name = models.CharField(max_length=200, blank=False, null=False)

# class Wheels(models.Model):
#     size = models.IntegerField()

# class Car(models.Model):
#     name = models.CharField(max_length=200, blank=False, null=False)
#     engine = models.OneToOneField(Engine, on_delete=models.CASCADE)
#     wheels = models.ForeignKey(Wheels, on_delete=models.CASCADE)

# Many to Many




