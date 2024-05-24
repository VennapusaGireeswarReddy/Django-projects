from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image= models.ImageField(upload_to='aha/image')
    video= models.FileField(upload_to='aha/videos')
    cast = models.TextField()

class Series(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image= models.ImageField(upload_to='aha/image')
    video= models.FileField(upload_to='aha/videos')
    cast = models.TextField()


def __str__(self):
        return self.name
# class Aha_user(models.Model):
#     username = models.CharField(max_length=50)
#     mobile = models.BigIntegerField()

