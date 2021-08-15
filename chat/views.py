# Create your views here.
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import user,conversation
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
def index(request):
    auser = request.session.get('user')
    contacts = []
    if auser is not None :
        contacts = user.objects.all().exclude(num = auser)
    return render(request,'chat/index.html',{'contacts':contacts})
def message(request):
    if request.method=="POST":
        msg = request.POST['message']   
        conversation(msgby = user.objects.get(user=request.user),msgtoadmin=True,msg=msg).save()
        return HttpResponse("{'msg':"+msg+"}")
    return redirect('index')  
def Login(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        userob = User.objects.filter(username = email)
        if userob.exists():
            USER = authenticate(request,username=email, password=password)
        else:
            userob = User.objects.create_user(email,email,password)
            userob.first_name  = name[0:name.find(' ')]
            userob.last_name  = name[name.find(' '):]
            userob.save()
            userob1 = user(user=userob,num=phone)
            userob1.save()
        USER = authenticate(request,username=email, password=password)
        if USER is not None:
            login(request, USER)
            messages.success(request, "successfully logged in")
            if request.GET.get('next') is not None:
                return redirect(request.GET.get('next'))
            return redirect('index')
        else:
            messages.error(request, "invalid credentials, please try again")
            return redirect('index')

    return redirect ('index')
def Logout(request):
    try:
        logout(request)
    except KeyError:
        pass
    return redirect("index")   
def getmsg(request):
    auser = request.user
    mlen = request.GET.get('len')
    messages = list(conversation.objects.filter(msgby__user=auser.id).order_by('time').values('msgby__user',
'msgtoadmin','msg'))
    if len(messages)==int(mlen):
        return HttpResponse("updated")
    return JsonResponse(messages[int(mlen):],safe=False)
