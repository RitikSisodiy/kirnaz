from django.contrib import admin
from . models import *

# Register your models here.


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display=('title',)

@admin.register(RegistrationSubMenu)
class RegistrationSubMenuAdmin(admin.ModelAdmin):
    list_display=('title','submenu')

@admin.register(SubRegistrationContent)
class SubRegistrationContentAdmin(admin.ModelAdmin):
    list_display=('reg_title',)

@admin.register(AboutRegistraionSubMenu)
class AboutRegistraionSubMenuAdmin(admin.ModelAdmin):
    list_display=('reg_title','heading1')

@admin.register(TitleSlide)
class TitleSlideAdmin(admin.ModelAdmin):
    list_display=('title',)

@admin.register(PackageIncluded)
class PackageIncludedAdmin(admin.ModelAdmin):
    list_display=('reg_title','heading1')

@admin.register(Procedure)
class ProcedureAdmin(admin.ModelAdmin):
    list_display=('reg_title','heading1')

@admin.register(DocumentRequired)
class DocumentRequiredAdmin(admin.ModelAdmin):
    list_display=('reg_title','heading1')

@admin.register(Memorandum)
class MemorandumAdmin(admin.ModelAdmin):
    list_display=('reg_title','heading1')

@admin.register(CompanyRegisterRequirements)
class CompanyRegisterRequirementsAdmin(admin.ModelAdmin):
    list_display=('reg_title','heading1')

@admin.register(Sainification)
class SainificationAdmin(admin.ModelAdmin):
    list_display=('reg_title','heading1')

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display=('reg_title','heading')
@admin.register(ourclients)
class FAQAdmin(admin.ModelAdmin):
    list_display=('reg_title','content')
@admin.register(contacts)
class contactsAdmin(admin.ModelAdmin):
    list_display=('reg_title','name','email','mobile','pincode')
