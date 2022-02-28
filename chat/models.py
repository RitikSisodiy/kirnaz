from email.policy import default
from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User
import time

from django.db.models.fields import related
def datetime_from_utc_to_local(utc_datetime):
    now_timestamp = time.time()
    offset = datetime.fromtimestamp(now_timestamp) - datetime.utcfromtimestamp(now_timestamp)
    return utc_datetime + offset
# Create your models here.
    
class user(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="user")
    phone = models.CharField(max_length=10,primary_key=True)
    alternative_Phone = models.CharField(max_length=10,blank=True)
    address = models.CharField(max_length=100,blank=True)
    profile = models.ImageField(upload_to='profile',default='profile/default.png')
    def __str__(self):
        return str(self.phone)
class conversation(models.Model):
    msgby = models.ForeignKey(user,related_name="msgby",on_delete=models.CASCADE,related_query_name="convo")
    msgtoadmin = models.BooleanField()
    msg = models.CharField(max_length=1000)
    readbyadmin = models.BooleanField(default=False)
    readbyuser = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now=True)
    def aunread(self):
        return conversation.objects.filter(msgby=self.msgby,readbyadmin=False).count()
    def uunread(self):
        return conversation.objects.filter(msgby=self.msgby,readbyuser=False).count()
    def msgtime(self):
        return datetime_from_utc_to_local(self.time).strftime('%I:%M')
class convofiles(models.Model):
    msg = models.ForeignKey(conversation,on_delete=models.SET_NULL,null=True,related_name='convofiles',)
    file = models.FileField(upload_to="convomedia")
    content_type = models.CharField(null=True, blank=True, max_length=100)
    def save(self, *args, **kwargs):
        try:
            self.content_type = self.file.file.content_type
        except:
            pass
        super().save(*args, **kwargs)
class Status(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="status")
    status = models.BooleanField(default=False)
    lastseen = models.DateTimeField(auto_now=True)
    def save(self, **kwargs):
        if not self.status:
            self.lastseen = timezone.now()
        super().save()
    def getLastSeen(self):
        return self.lastseen.__str__()