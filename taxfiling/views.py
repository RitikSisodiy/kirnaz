from django.shortcuts import render, redirect
from taxfiling.models import *

# Create your views here.

def taxfiling(request,slug1):

    tax = TaxFiling.objects.get(slug=slug1)
    return render(request,'taxfiling.html',{'reg':tax,})