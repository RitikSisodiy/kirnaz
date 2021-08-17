from ckeditor.fields import RichTextField
from django.db import models
from django.db.models.deletion import SET_NULL
from django.http import request
from registration.models import RegistrationSubMenu
from othernavs.models import RegistrationSubMenu as othernavsubmenu
# Create your models here.

class Slider(models.Model):
    objective = models.CharField(max_length=100)
    obj_details = models.TextField()
    img = models.ImageField(upload_to="img")
class aboutca(models.Model):
    title = models.CharField(max_length=50)
    content = RichTextField(blank=True,null=True)

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
class links(models.Model):
    title = models.CharField(max_length=50)
    page1 = models.ForeignKey(RegistrationSubMenu,on_delete=models.SET_NULL,blank=True,null=True)
    orpage2 = models.ForeignKey(othernavsubmenu,on_delete=models.SET_NULL,blank=True,null=True)
class Expertise(models.Model):
    icon = models.ImageField(upload_to="imgaes")
    title = models.CharField(max_length=50)
class marketplace(models.Model):
    icon = models.FileField(upload_to="imgaes")
    title = RichTextField(blank=True,null=True)
class addblog(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="blogsimg")
    content = RichTextField(blank=True,null=True)
    time = models.DateTimeField(auto_now=True)