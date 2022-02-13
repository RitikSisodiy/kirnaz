from statistics import mode
from django.db import models
from datetime import datetime
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
    profile = models.ImageField(upload_to='profile',blank='true')
    def __str__(self):
        return str(self.user.id)
class conversation(models.Model):
    msgby = models.ForeignKey(user,related_name="msgby",on_delete=models.CASCADE,related_query_name="convo")
    msgtoadmin = models.BooleanField()
    msg = models.CharField(max_length=1000)
    time = models.DateTimeField(auto_now=True)
    def msgtime(self):
        return datetime_from_utc_to_local(self.time).strftime('%I:%M')
class convofiles(models.Model):
    msg = models.ForeignKey(conversation,on_delete=models.SET_NULL,null=True,related_name='convofiles',)
    file = models.FileField(upload_to="convomedia")
class Status(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="status")
    status = models.BooleanField(default=False)