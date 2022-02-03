from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from registration.models import unique_slug_generator
from django.urls import reverse
# Create your models here.
from registration.models import icon
class Registration(models.Model):
    title = models.CharField(max_length=50)
    logo = models.ImageField(upload_to="logos",blank=True)
    # content = models.CharField(max_length=5000)
    info = models.CharField(max_length=100,blank=True)
    slug = models.SlugField(blank=True)
    def save(self, *args, **kwargs):
        self.slug = unique_slug_generator(Registration,self.title)
        super(Registration, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

from django.contrib.contenttypes.fields import GenericRelation
from registration.models import BlogNews  
class RegistrationSubMenu(models.Model):
    title = models.ForeignKey(Registration, on_delete=models.CASCADE ,related_name="RegistrationSubMenu")
    submenu = models.CharField(max_length=50)
    tags = GenericRelation(BlogNews,related_query_name='reg_title')
    logo = models.ImageField(upload_to="logos",blank=True)
    slug = models.SlugField(blank=True)
    def save(self, *args, **kwargs):
        self.slug = unique_slug_generator(RegistrationSubMenu,self.submenu)
        super(RegistrationSubMenu, self).save(*args, **kwargs)
    def __str__(self) :
        return str(self.title.slug+"/"+self.slug)
    def getabsoluteurl(self):
        return reverse('handlenav',kwargs={'slug1': self.title.slug,'slug2':self.slug})

    class Meta:
        unique_together = [['title', 'submenu']]


class ourclients(models.Model):
    reg_title = models.ForeignKey(RegistrationSubMenu, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    Profile = models.ImageField(upload_to="clients")
    SignatureOptional = models.ImageField(upload_to="clientsign",blank=True)
    content = models.TextField(null=True,blank=True)

class SubRegistrationContent(models.Model):
    reg_title = models.ForeignKey(RegistrationSubMenu, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    formtitle= models.CharField(max_length=500)
    subtitle = models.CharField(max_length=500)
    Content = RichTextField(null=True,blank=True)
    # heading1 = models.CharField(max_length=500,null=True,blank=True)
    # heading1_details = models.TextField(null=True,blank=True)
    # heading2 = models.CharField(max_length=500,null=True,blank=True)
    # heading2_details = models.TextField(null=True,blank=True)
    # heading3 = models.CharField(max_length=500,null=True,blank=True)
    # heading3_details = models.TextField(null=True,blank=True)
    BannerImg = models.ImageField(upload_to = 'img',blank=True)
    def __str__(self):
        return str(self.title)
class AboutRegistraionSubMenu(models.Model):
    reg_title = models.ForeignKey(RegistrationSubMenu, on_delete=models.CASCADE)
    heading1 = models.CharField(max_length=500,null=True,blank=True)
    heading1_details = RichTextField(null=True,blank=True)
    heading2 = models.CharField(max_length=500,null=True,blank=True)
    heading2_details = RichTextField(null=True,blank=True)
    Optionalicon = models.ImageField(upload_to = 'img',blank=True)


class TitleSlide(models.Model):
    title = models.CharField(max_length=50,default='')

class PackageIncluded(models.Model):
    reg_title = models.ForeignKey(RegistrationSubMenu, on_delete=models.CASCADE)
    heading1 = models.CharField(max_length=500,null=True,blank=True)
    icon = models.ForeignKey(icon,on_delete=models.SET_NULL,null=True,related_name='othernavicon')


class Procedure(models.Model):
    reg_title = models.ForeignKey(RegistrationSubMenu, on_delete=models.CASCADE)
    heading1 = models.CharField(max_length=500,null=True,blank=True)
    content = models.CharField(max_length=500)
    icon = models.ForeignKey(icon,on_delete=models.SET_NULL,null=True,related_name="Othernavicon")

class DocumentRequired(models.Model):
    reg_title = models.ForeignKey(RegistrationSubMenu, on_delete=models.CASCADE)
    heading1 = models.CharField(max_length=500,null=True,blank=True)
    content = RichTextField(null=True,blank=True)


class Memorandum(models.Model):
    reg_title = models.ForeignKey(RegistrationSubMenu, on_delete=models.CASCADE)
    heading1 = models.CharField(max_length=500,null=True,blank=True)
    content = RichTextField(null=True,blank=True)



class CompanyRegisterRequirements(models.Model):
    reg_title = models.ForeignKey(RegistrationSubMenu, on_delete=models.CASCADE)
    heading1 = models.CharField(max_length=500,null=True,blank=True)
    content1 = RichTextField(null=True,blank=True)
    heading2 = models.CharField(max_length=500,null=True,blank=True)
    content2 = RichTextField(null=True,blank=True)


class Sainification(models.Model):
    reg_title = models.ForeignKey(RegistrationSubMenu, on_delete=models.CASCADE)
    heading1 = models.CharField(max_length=500,null=True,blank=True)
    content2 = RichTextField(null=True,blank=True)


class FAQ(models.Model):
    reg_title = models.ForeignKey(RegistrationSubMenu, on_delete=models.CASCADE)
    heading = models.CharField(max_length=500,null=True,blank=True)
    # content = models.TextField(null=True,blank=True)
    content = RichTextField(null=True,blank=True)

class contacts(models.Model):
    reg_title = models.ForeignKey(RegistrationSubMenu, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    pincode = models.CharField(max_length=50)
    time = models.DateTimeField(auto_now=True)
