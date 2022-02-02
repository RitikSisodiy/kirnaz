from distutils.command.upload import upload
from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from django.urls import reverse
from datetime import datetime
# Create your models here.
import random ,string
def get_random_string(size):
    return ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k = size))

def unique_slug_generator(instance, new_slug=None):
    """
    This is for a Django project and it assumes your instance 
    has a model with a slug field and a title character (char) field.
    """
    slug=new_slug
    Klass = instance
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = slugify(str(slug)+get_random_string(4))
        return unique_slug_generator(instance, new_slug=new_slug)
    return slugify(slug)

class iconver(models.Model):
    version = models.CharField(max_length=50)
class icon(models.Model):
    version = models.ForeignKey(iconver,on_delete=models.SET_NULL,null=True)
    icon = models.CharField(max_length=70)
    def __str__(self):
        return self.icon

class Registration(models.Model):
    title = models.CharField(max_length=50)
    # content = models.CharField(max_length=5000)
    slug = models.SlugField(blank=True)
    type = models.CharField(max_length=1,choices=((1,'registration'),(2,'othernavs')))
    def save(self, *args, **kwargs):
        self.slug = unique_slug_generator(Registration,self.title)
        super(Registration, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation
class BlogNews(models.Model):
    Tchoice = (
        ('1','News'),
        ('2','Blogs'),
        ('3','Article'),
    )
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    # reg_title = models.ForeignKey(RegistrationSubMenu, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    last_update = models.DateTimeField(auto_now=True)
    type = models.CharField(max_length=1, choices=Tchoice)
    img = models.ImageField(upload_to='blogs')
    title= models.CharField(max_length=200,null=True,blank=True)
    Short_des = models.CharField(max_length=500)
    content = RichTextField()
    slug = models.SlugField(blank=True)
    def save(self, *args, **kwargs):
        if self.slug is None or len(self.slug)==0:
            self.slug = unique_slug_generator(BlogNews,self.title)
        self.last_update = datetime.now()
        super(BlogNews, self).save(*args, **kwargs)
    def Getchoices(self):
        return self.Tchoice
    def getabsoluteurl(self):
        return reverse('singleblog',kwargs={'slug': dict(self.Tchoice)[self.type],'slug1':self.slug})

    
class RegistrationSubMenu(models.Model):
    title = models.ForeignKey(Registration, on_delete=models.CASCADE ,related_name="RegistrationSubMenu")
    logo = models.ImageField(upload_to="logos",blank=True)
    tags = GenericRelation(BlogNews,related_query_name='reg_title1')
    slug = models.SlugField(blank=True)
    submenu = models.CharField(max_length=50)
    def save(self, *args, **kwargs):
        self.slug = unique_slug_generator(RegistrationSubMenu,self.submenu)
        super(RegistrationSubMenu, self).save(*args, **kwargs)
    def __str__(self) :
        return str(self.title.slug+"/"+self.slug)
    class Meta:
        unique_together = [['title', 'submenu']]
    def getabsoluteurl(self):
        return reverse('registration',kwargs={'slug1': self.title.slug,'slug2':self.slug})


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
    icon = models.ForeignKey(icon,on_delete=models.SET_NULL,null=True)


class Procedure(models.Model):
    reg_title = models.ForeignKey(RegistrationSubMenu, on_delete=models.CASCADE)
    heading1 = models.CharField(max_length=500,null=True,blank=True)
    content = models.CharField(max_length=500)
    icon = models.ForeignKey(icon,on_delete=models.SET_NULL,null=True)

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

class aboutContent(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField(max_length=5000 ,null=True,blank=True)
    img = models.ImageField(upload_to="about",blank=True)
