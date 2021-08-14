from django.db import models

# Create your models here.

class Slider(models.Model):
    objective = models.CharField(max_length=100)
    obj_details = models.TextField()
    img = models.ImageField(upload_to="img")


class BusinessQuery(models.Model):
    name = models.CharField(max_length=30)
    phone = models.IntegerField()
    email = models.EmailField(max_length=50)
    message = models.CharField(max_length=500)

class News(models.Model):
    date = models.DateField(auto_now_add=False,null=True,blank=True)
    news = models.TextField()

class DueDateReminder(models.Model):
    date = models.DateField(auto_now_add=False,null=True,blank=True)
    details = models.TextField()

class BlogNews(models.Model):
    date = models.DateField(auto_now_add=False,null=True,blank=True)
    title= models.CharField(max_length=50,null=True,blank=True)
    news = models.TextField()

class Offrings(models.Model):
    title = models.CharField(max_length=100)
    details = models.CharField(max_length=500)
    img = models.ImageField(upload_to="img")