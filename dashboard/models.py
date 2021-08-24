from django.contrib.auth.models import User
from django.db import models
from django.db.models import fields
from registration.models import RegistrationSubMenu
from othernavs.models import RegistrationSubMenu as othernavRegistrationSubMenu
# Create your models here.
class Sections(models.Model):
    reg_title = models.OneToOneField(RegistrationSubMenu,on_delete=models.CASCADE)
    section = models.CharField(max_length=1000,default='["Top Form section","Included in Our Packge","Procedure","Package icon","document","Memorandum","Register","FAQS","Signification","Our Clients"]')
class Sectionsothernavs(models.Model):
    reg_title = models.OneToOneField(othernavRegistrationSubMenu,on_delete=models.CASCADE)
    section = models.CharField(max_length=1000,default='["Top Form section","Included in Our Packge","Procedure","Package icon","document","Memorandum","Register","FAQS","Signification","Our Clients"]')
class makepaymentrequest(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    reason = models.CharField(max_length=100)
    ammount = models.FloatField()
    status = models.CharField(max_length=20,default="pending")