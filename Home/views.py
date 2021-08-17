from dashboard.homeforms import aboutcaform
from django.contrib import messages
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from . models import *
from registration.models import *
from taxfiling.models import *
from django.contrib.auth import authenticate, login, logout


def index(request):
    slider = Slider.objects.all()
    news = News.objects.all()
    ddreminder = DueDateReminder.objects.all()
    bnews = BlogNews.objects.all()
    offrings = Offrings.objects.all()
    menu = RegistrationSubMenu.objects.all()
    abca = aboutca.objects.all()
    abca = abca[0] if abca.exists() else []
    latestblog = addblog.objects.all()
    latestblog = latestblog.order_by('time')[0] if latestblog.exists() else []
    res = { 
        'slider':slider,
        "aboutca":abca ,
        'news':news,
        'ddreminder':ddreminder,
        'bnews':bnews,
        'offrings':offrings,
        'menu':menu,
        'latestblog': latestblog
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
    res= {}
    res["banner"]= headbanner.objects.all()[0]
    res["links"]= links.objects.all()
    res["exper"]= Expertise.objects.all()
    res["marketplace"]= marketplace.objects.all()
    return render(request,'about.html',res)

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

def Login(request):
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
def logindashboard(request):
    print("hellp this funtion is working")
    if request.method=="POST":
        print(request.POST,"this is working")
        username = request.POST.get('username')
        password = request.POST.get('password')
        USER = authenticate(request,username=username, password=password)
        if USER is not None:
            login(request, USER)
            if request.user.is_superuser:
                return JsonResponse({'status':'ok'})
            return JsonResponse({"status":'invaliduser'})
    return render(request,'logindashboard.html')