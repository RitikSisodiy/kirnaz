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
class headbanner(models.Model):
    banner_title = models.CharField(max_length=500,blank=True)
    banner_content = models.CharField(max_length=1500,blank=True)
    banneerimg = models.ImageField(upload_to="banner",blank=True)