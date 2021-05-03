from django.db import models
from django.utils import timezone

# Create your models here.

class Owner(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(blank=True, null=True)


class Vaccine(models.Model):
    name = models.CharField(max_length = 200)
    date = models.DateTimeField(blank = True, null = True)
    def __str__(self):
        return self.name

class Race(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Pet(models.Model):
    name = models.CharField(max_length=200)
    race = models.ForeignKey('Race', on_delete=models.CASCADE)
    date_of_birth=models.DateTimeField(blank=True, null=True)
    owner = models.ForeignKey('Owner', on_delete=models.CASCADE)
    vaccine = models.ForeignKey('Vaccine', on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    date_of_birth=models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
