from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from registration.models import *
from ckeditor.widgets import CKEditorWidget

class section0Form(ModelForm):
    class Meta:
        model = SubRegistrationContent
        exclude = ('id',)    
        widgets = {'reg_title': forms.HiddenInput()}    
class PackageIncludedForm(ModelForm):
    class Meta:
        model = PackageIncluded
        exclude = ('id',)    
        widgets = {'reg_title': forms.HiddenInput(),'icon':forms.HiddenInput()}    
class section1Form(ModelForm):
    class Meta:
        model = AboutRegistraionSubMenu
        exclude = ('id',)    
        widgets = {'reg_title': forms.HiddenInput()}    

class section2Form(ModelForm):
    class Meta:
        model = DocumentRequired
        exclude = ('id',)    
        widgets = {'reg_title': forms.HiddenInput()}    
class section3Form(ModelForm):
    class Meta:
        model = Procedure
        exclude = ('id',)
        widgets = {'reg_title': forms.HiddenInput(),'icon':forms.HiddenInput()}    

class section4Form(ModelForm):
    class Meta:
        model = Memorandum
        exclude = ('id',)    
        widgets = {'reg_title': forms.HiddenInput()}    
class section5Form(ModelForm):
    class Meta:
        model = CompanyRegisterRequirements
        exclude = ('id',)    
        widgets = {'reg_title': forms.HiddenInput()}    
class section6Form(ModelForm):
    class Meta:
        model = FAQ
        exclude = ('id',)    
        widgets = {'reg_title': forms.HiddenInput()}    
class section7Form(ModelForm):
    class Meta:
        model = Sainification
        exclude = ('id',)    
        widgets = {'reg_title': forms.HiddenInput()}    

class section8Form(ModelForm):
    class Meta:
        model = ourclients
        exclude = ('id',)    
        widgets = {'reg_title': forms.HiddenInput()}    
class section9Form(ModelForm):
    class Meta:
        model = BlogNews
        exclude = ('id','content_type','object_id')   
    

# class userRegister(ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput,label='Password')
#     def __init__(self, *args, **kwargs):
#         super(userRegister, self).__init__(*args, **kwargs)
#         for field_name in self.fields:
#             field = self.fields.get(field_name)  
#             if field:
#                 if type(field.widget) in (forms.TextInput, forms.DateInput,forms.EmailInput):
#                     field.widget = forms.TextInput(attrs={'placeholder':  field.label})
#                 if type(field.widget) in (forms.PasswordInput,):
#                     field.widget = forms.PasswordInput(render_value=False, attrs={'placeholder': 'password'})
#     class Meta:
#         model = User
#         fields = ['first_name','last_name','email','password']
#     def clean_email(self):
#         email = self.cleaned_data.get('email')
#         username = self.cleaned_data.get('username')
#         if email and User.objects.filter(email=email).exclude(username=username).exists():
#             raise forms.ValidationError(u'Ths Email addresses is already exist')
#         return email
        
# class StaffRegister(ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(StaffRegister, self).__init__(*args, **kwargs)
#         for field_name in self.fields:
#             field = self.fields.get(field_name)  
#             if field:
#                 if type(field.widget) in (forms.TextInput, forms.DateInput,forms.EmailInput,forms.PasswordInput):
#                     field.widget = forms.TextInput(attrs={'placeholder':  field.label})
#                 if type(field.widget) in (forms.PasswordInput,):
#                     field.widget = forms.PasswordInput(render_value=False, attrs={'placeholder': 'password'})
#     class Meta:
#         model = staffregister
#         exclude = ('user','status','phonestatus')
#     def clean_phone(self):
#         phone = self.cleaned_data['phone']
#         phone = str(phone).replace('+91','')
#         phone = str(phone).replace(' ','')
#         if phone[0] == '0':
#             phone = phone[1:]
#         print(phone)
#         if len(phone)==10:
#             return phone
#         else:
#             raise forms.ValidationError("enter the valid phone number")
# class StudentRegister(ModelForm):
        
#     def __init__(self, *args, **kwargs):
#         super(StudentRegister, self).__init__(*args, **kwargs)
#         for field_name in self.fields:
#             field = self.fields.get(field_name)  
#             if field:
#                 if type(field.widget) in (forms.TextInput, forms.DateInput,forms.EmailInput,forms.PasswordInput):
#                     field.widget = forms.TextInput(attrs={'placeholder':  field.label})
#                 if type(field.widget) in (forms.PasswordInput,):
#                     field.widget = forms.PasswordInput(render_value=False, attrs={'placeholder': 'password'})
#     class Meta:
#         model = studentregister
#         exclude = ('user','status','phonestatus')
        
# class loginform(forms.Form):
#     username = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder':'Enter the email'}))
#     password = forms.CharField(widget=forms.PasswordInput(render_value=False, attrs={'placeholder': 'password'}),max_length=30)
    
#     def clean_username(self):
#         username = self.cleaned_data['username']
#         print(username)
#         if User.objects.filter(email=username).exists() is False:
#             raise forms.ValidationError("this mail is not registered")
#         else:
#             return username
# class otpform(forms.Form):
#     otp = forms.CharField(max_length=10,widget=forms.TextInput(attrs={'placeholder':'Enter the OTP'}))


from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.admin import (
      widgets,
      site as admin_site
    )

def GenForm(Model,listHiddenfield=[],disablefield=[]):
    data = {field:forms.HiddenInput() for field in listHiddenfield}
    class newform(forms.ModelForm):
        class Meta:
            model = Model
            exclude = ('id',)
            widgets = data
        def __init__(self, *args, **kwargs):
            super(newform, self).__init__(*args, **kwargs)
            for f in Model._meta.fields:
                if "DateTimeField" in str(type(f)):
                    print('DateTimeField is present',f.name)
                    try:
                        self.fields[f.name].widget.attrs['class'] = 'vDateTime'
                    except Exception:
                        pass
                if "ForeignKey" in str(type(f)):
                    print('ForeignKey is present',f.name)
                    try:
                        self.fields[f.name].widget  = widgets.RelatedFieldWidgetWrapper(
                        self.fields[f.name].widget,
                        self.instance._meta.get_field(f.name).remote_field,
                        admin_site
                    )
                    except Exception:
                        pass
                if "ManyToManyField" in str(type(f)):
                    print('ManyToManyField is present',f.name)
                    try:
                        pass
                    except Exception:
                        pass 
                           
    return newform  