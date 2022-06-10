from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    photo = models.ImageField(upload_to='photos')
    specs = models.FileField(upload_to='specs')
