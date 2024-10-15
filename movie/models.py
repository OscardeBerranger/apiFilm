import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Model



class CustomUser(AbstractUser):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    enabled = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class Author(models.Model):
    name = models.CharField(max_length=100)
    firstName = models.CharField(max_length=100)
    birthDate = models.DateField()

class Genre(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    publishedDate = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre)
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

