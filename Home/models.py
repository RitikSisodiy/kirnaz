from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import SET_NULL
from django.http import request
from registration.models import RegistrationSubMenu
from othernavs.models import RegistrationSubMenu as othernavsubmenu
from dashboard.models import makepaymentrequest
# Create your models here.
from datetime import datetime
class Slider(models.Model):
    objective = models.CharField(max_length=100)
    obj_details = models.TextField()
    img = models.ImageField(upload_to="img")
    def __str__(self) -> str:
        return self.objective
class aboutca(models.Model):
    title = models.CharField(max_length=50)
    content = RichTextField(blank=True,null=True)
    def __str__(self) -> str:
        return self.title
class ContactDetails(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    address = models.TextField(max_length=100)
    otherPhones = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.email
class BusinessQuery(models.Model):
    name = models.CharField(max_length=30)
    phone = models.IntegerField()
    email = models.EmailField(max_length=50)
    message = models.CharField(max_length=500)
    def __str__(self) -> str:
        return self.name
class News(models.Model):
    date = models.DateField(auto_now_add=False,null=True,blank=True)
    news = models.TextField()
    def __str__(self) -> str:
        return self.date
class DueDateReminder(models.Model):
    date = models.DateField(auto_now_add=False,null=True,blank=True)
    details = models.TextField()
    def __str__(self) -> str:
        return self.date
class BlogNews(models.Model):
    Tchoice = (
        ('1','News'),
        ('2','Blogs'),
        ('3','Article'),
    )
    date = models.DateTimeField(auto_now=True)
    last_update = models.DateTimeField(auto_now=True)
    type = models.CharField(max_length=1, choices=Tchoice)
    img = models.ImageField(upload_to='blogs')
    title= models.CharField(max_length=200,null=True,blank=True)
    Short_des = models.CharField(max_length=500)
    content = RichTextField()
    def save(self, *args, **kwargs):
        self.last_update = datetime.now()
        super(BlogNews, self).save(*args, **kwargs)
    def Getchoices(self):
        return self.Tchoice
    def __str__(self) -> str:
        return self.title
class Offrings(models.Model):
    title = models.CharField(max_length=100)
    details = models.CharField(max_length=500)
    img = models.ImageField(upload_to="img")
    def __str__(self) -> str:
        return self.title
class headbanner(models.Model):
    banner_title = models.CharField(max_length=500,blank=True)
    banner_content = models.CharField(max_length=1500,blank=True)
    banneerimg = models.ImageField(upload_to="banner",blank=True)
    def __str__(self) -> str:
        return self.banner_title
class links(models.Model):
    title = models.CharField(max_length=50)
    page1 = models.ForeignKey(RegistrationSubMenu,on_delete=models.SET_NULL,blank=True,null=True)
    orpage2 = models.ForeignKey(othernavsubmenu,on_delete=models.SET_NULL,blank=True,null=True)
    def __str__(self) -> str:
        return self.title
class Expertise(models.Model):
    icon = models.ImageField(upload_to="imgaes")
    title = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.title
class marketplace(models.Model):
    icon = models.FileField(upload_to="imgaes")
    title = RichTextField(blank=True,null=True)
    def __str__(self) -> str:
        return self.title
class addblog(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="blogsimg")
    content = RichTextField(blank=True,null=True)
    time = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return self.title
class Payments(models.Model):
    order_id = models.CharField(unique=True, max_length=100, null=True, blank=True, verbose_name="Payments")
    payreq = models.ForeignKey(makepaymentrequest,on_delete=models.SET_NULL,null=True)
    ammount = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50,default='pending')
    other_data = models.CharField(max_length=1000,default="nodata")
    def save(self, *args, **kwargs):
        if self.order_id is None and self.order_date and self.id:
            self.order_id = self.order_date.strftime('PAY2ME%Y%m%dODR') + str(self.id)
        return super().save(*args, **kwargs)
    def __str__(self) -> str:
        return self.order_id
class documents(models.Model):
    user = models.ForeignKey(User,on_delete=SET_NULL,null=True)
    name = models.CharField(max_length=100)
    doc = models.FileField(upload_to="documents")
    time = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return self.name
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class TaggedItem(models.Model):
    tag = models.SlugField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):              # __unicode__ on Python 2
        return self.tag