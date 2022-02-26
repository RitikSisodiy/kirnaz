from django.contrib.auth.models import User
from django.db import models
from django.db.models import fields
from registration.models import RegistrationSubMenu
from othernavs.models import RegistrationSubMenu as othernavRegistrationSubMenu

# Create your models here.
class Sections(models.Model):
    reg_title = models.OneToOneField(RegistrationSubMenu,on_delete=models.CASCADE)
    section = models.CharField(max_length=1000,default='["Top Form section","Included in Our Packge","Procedure","Package icon","document","Memorandum","Register","FAQS","Signification","Our Clients"]')
    def __str__(self) -> str:
        return self.section
class Sectionsothernavs(models.Model):
    reg_title = models.OneToOneField(othernavRegistrationSubMenu,on_delete=models.CASCADE)
    section = models.CharField(max_length=1000,default='["Top Form section","Included in Our Packge","Procedure","Package icon","document","Memorandum","Register","FAQS","Signification","Our Clients"]')
    def __str__(self) -> str:
        return self.section
class makepaymentrequest(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    reason = models.CharField(max_length=100)
    ammount = models.FloatField()
    status = models.CharField(max_length=20,default="pending")
    def __str__(self) -> str:
        return self.reason
class aboutContact(models.Model):
    logo = models.ImageField(upload_to="logo")
    AdminTitle = models.CharField(max_length=30)
    favicon  = models.ImageField(upload_to='logo')
    def __str__(self) -> str:
        return self.AdminTitle

class emailSetup(models.Model):
    host = models.CharField(max_length=100)
    port = models.IntegerField()
    email = models.CharField(max_length=100)
    tsl = models.BooleanField()
    ssl = models.BooleanField()
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    activate = models.BooleanField(help_text="other mail is automatically disabled")
    def save(self, *args, **kwargs):
        if self.activate:
            data=emailSetup.objects.all().exclude(id=self.id)
            data.update(activate=False)
        super(emailSetup, self).save(*args, **kwargs)
    def __str__(self) -> str:
        return self.email