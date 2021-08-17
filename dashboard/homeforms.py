from Home.models import *
from django import forms
from django.contrib.admin import widgets
class sliderform(forms.ModelForm):
    class Meta:
        model = Slider
        exclude = ('id',)    
class aboutcaform(forms.ModelForm):
    class Meta:
        model = aboutca
        exclude = ('id',)    
class BlogNewsform(forms.ModelForm):
    class Meta:
        model = BlogNews
        exclude = ('id',)    
class DueDateReminderform(forms.ModelForm):
    date = forms.DateField(widget=widgets.AdminDateWidget)
    class Meta:
        model = DueDateReminder
        exclude = ('id',)    
class Newsform(forms.ModelForm):
    date = forms.DateField(widget=widgets.AdminDateWidget)
    class Meta:
        model = News
        exclude = ('id',)    
class addblogform(forms.ModelForm):
    class Meta:
        model = addblog
        exclude = ('id','time')    
        