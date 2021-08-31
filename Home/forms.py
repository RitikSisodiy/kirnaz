from django import forms
from django.contrib.auth import models
from django.forms import ModelForm, widgets
from django.contrib.auth.models import User
from chat.models import user

class Userform(ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email']
    def __init__(self, *args, **kwargs):
        super(Userform, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
class userform(ModelForm):
    class Meta:
        model = user
        fields = ['user','phone','alternative_Phone','address','profile']
        widgets = {'user':forms.HiddenInput()}
    def __init__(self, *args, **kwargs):
        super(userform, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
