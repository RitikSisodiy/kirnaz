from django.contrib import admin
from . models import *
# Register your models here.

@admin.register(TaxFiling)
class TaxFilingAdmin(admin.ModelAdmin):
    list_display=('title',)