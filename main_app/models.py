from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Pet(models.Model):
    name = models.CharField(max_length=30)
    type_of_animal = models.CharField(max_length=50)
    breed = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    profile_picture = models.CharField(max_length=200)


class Post(models.Model):
    image = models.CharField(max_length=250)
    caption = models.TextField(max_length=250)
    likes = models.IntegerField()
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)