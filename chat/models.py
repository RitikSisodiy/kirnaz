from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
import time
def datetime_from_utc_to_local(utc_datetime):
    now_timestamp = time.time()
    offset = datetime.fromtimestamp(now_timestamp) - datetime.utcfromtimestamp(now_timestamp)
    return utc_datetime + offset
# Create your models here.
class user(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    num = models.CharField(max_length=10,primary_key=True)
    def __str__(self):
        return str(self.user.id)
class conversation(models.Model):
    msgby = models.ForeignKey(user,related_name="msgby",on_delete=models.CASCADE)
    msgtoadmin = models.BooleanField()
    msg = models.CharField(max_length=1000)
    time = models.DateTimeField(auto_now=True)
    def msgtime(self):
        return datetime_from_utc_to_local(self.time).strftime('%I:%M')