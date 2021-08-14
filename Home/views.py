from django.shortcuts import render
from . models import *
from registration.models import *
from taxfiling.models import *


def index(request):
    slider = Slider.objects.all()
    news = News.objects.all()
    ddreminder = DueDateReminder.objects.all()
    bnews = BlogNews.objects.all()
    offrings = Offrings.objects.all()
    menu = RegistrationSubMenu.objects.all()


    res = { 
        'slider':slider,
        'news':news,
        'ddreminder':ddreminder,
        'bnews':bnews,
        'offrings':offrings,
        'menu':menu,
    }
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        data = BusinessQuery(name=name, email=email, phone=phone, message=message)
        data.save()
    return render(request,'index.html',res)

def about(request):
    return render(request,'about.html')

def another(request):
    return render(request,'another.html')

def blogpage(request):
    return render(request,'blog-page.html')

def blog(request):
    return render(request,'blog.html')

def chatbox(request):
    return render(request,'chatbox.html')

def companyregistration(request):
    return render(request,'companyregistration.html')

def incometaxfilling(request):
    return render(request,'incomeTaxFilling.html')

def login(request):
    return render(request,'login.html')

def memberlogin(request):
    return render(request,'member-login.html')

def membersignup(request):
    return render(request,'member-signup.html')

def newsfeed(request):
    return render(request,'newsfeed.html')

def pvtltdreg(request):
    return render(request,'pvt-ltd-reg.html')

# def privateltdreg(request):
#     return render(request,'pvtrivateltdreg.html')

def signup(request):
    return render(request,'signup.html')

def signup1(request):
    return render(request,'signup1.html')

def signup2(request):
    return render(request,'signup2.html')