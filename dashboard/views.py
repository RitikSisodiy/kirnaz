from django.urls.conf import path
from Home.views import blog
from chat.models import conversation
from django.http import request
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from registration.models import *
from .forms import *
from .models import *
import json
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout

from cflax.settings import sectionname

from django.contrib.contenttypes.models import ContentType
from .dashboardsettings import templateFolder

# Create your views here.
def GetContentType(model):
    return ContentType.objects.get(app_label=model._meta.app_label, model=model._meta.model_name)

def index(request):
    res = {}
    res["title"] = "Dashboard"
    try:
        return render(request,f'{templateFolder}/extra/dashboard.html',res)
    except Exception:    
        return render(request,'dashboard.html',res)
def registration(request,slug=None):
    res = {}
    if slug is not None:
        res['registration'] = Registration.objects.filter(slug=slug)
    else:
        res['registration'] = Registration.objects.all()
    res["title"] = "Registration"
    try:
        return render(request,f'{templateFolder}/extra/dregistrations.html',res)
    except Exception:    
        return render(request,'dregistrations.html',res)
sections = [SubRegistrationContent,AboutRegistraionSubMenu,DocumentRequired,PackageIncluded,Procedure,Memorandum,CompanyRegisterRequirements,FAQ,Sainification,ourclients,BlogNews]
# adding multi objects form as a list in sectionsform
sectionsforms = [section0Form,section1Form,section2Form,[PackageIncludedForm],[section3Form],section4Form,section5Form,[section6Form],section7Form,[section8Form],[section9Form]]

def editregistration(request,slug1,slug2):
    RegistrationSubMenuob = RegistrationSubMenu.objects.get(slug=slug2,title__slug=slug1)
    s = []
    for i in sections:
        try:
            s.append(i.objects.filter(reg_title = RegistrationSubMenuob) if i.objects.filter(reg_title = RegistrationSubMenuob).exists() else [None] )
        except:
            s.append(i.objects.filter(reg_title1 = RegistrationSubMenuob) if i.objects.filter(reg_title1 = RegistrationSubMenuob).exists() else [None] )
    # s1 = sections[0].objects.filter(reg_title = RegistrationSubMenuob) if sections[0].objects.filter(reg_title = RegistrationSubMenuob).exists()  else [RegistrationSubMenuob]
    # s2 = sections[1].objects.filter(reg_title = RegistrationSubMenuob) if sections[1].objects.filter(reg_title = RegistrationSubMenuob).exists()  else [RegistrationSubMenuob]
    # s3 = sections[2].objects.filter(reg_title = RegistrationSubMenuob) if sections[2].objects.filter(reg_title = RegistrationSubMenuob).exists()  else [RegistrationSubMenuob]
    # s4 = sections[3].objects.filter(reg_title = RegistrationSubMenuob) if sections[3].objects.filter(reg_title = RegistrationSubMenuob).exists()  else [RegistrationSubMenuob]
    # s5 = sections[4].objects.filter(reg_title = RegistrationSubMenuob) if sections[4].objects.filter(reg_title = RegistrationSubMenuob).exists()  else [RegistrationSubMenuob]
    # s6 = sections[5].objects.filter(reg_title = RegistrationSubMenuob) if sections[5].objects.filter(reg_title = RegistrationSubMenuob).exists()  else [RegistrationSubMenuob]
    # s7 = sections[6].objects.filter(reg_title = RegistrationSubMenuob) if sections[6].objects.filter(reg_title = RegistrationSubMenuob).exists()  else [RegistrationSubMenuob]

    res = {}
    res['title'] = "Edit Registrations"
    li = []
    for i in range(0,len(sectionsforms)):
        if isinstance(sectionsforms[i],list):
            new = [sectionsforms[i][0](instance= j,initial={'reg_title': RegistrationSubMenuob}) for j in s[i]]
            new.append(sectionsforms[i][0](initial={'reg_title': RegistrationSubMenuob}))
            li.append(new)
        else:
            li.append(sectionsforms[i](instance= s[i][0],initial={'reg_title': RegistrationSubMenuob}))
    # li.append(section1Form(instance= s[0][0]))
    # li.append(section2Form(instance= s[1][0]))
    # li.append([section3Form(instance= i) for i in s[2]])
    # li.append(section4Form(instance= s[3][0]))
    # li.append(section5Form(instance= s[4][0]))
    # li.append([section6Form(instance= i) for i in s[5]])
    # li.append(section7Form(instance= s[6][0]))
    if request.method == "POST":
        page_number = int(request.GET.get('page') if request.GET.get('page') is not None else 1) - 1
        objectno = (request.GET.get('object') if request.GET.get('object') is not None else 1)
        if request.GET.get('object') is None:
            form = sectionsforms[page_number](request.POST,request.FILES,instance=s[page_number][0])
        else:
            if sectionsforms[page_number] is None or objectno == "new":
                form = sectionsforms[page_number][0](request.POST,request.FILES,instance = None)
            else:
                form = sectionsforms[page_number][0](request.POST,request.FILES,instance = s[page_number].filter(id=objectno)[0])
        if form.is_valid():
            form = form.save(commit=False)
            try:
                form.content_type =GetContentType(RegistrationSubMenuob)
                form.object_id = RegistrationSubMenuob.id
            except Exception as e:
                print("exception +++++++",e)
                pass
            form.save()
            messages.success(request,"Information Is Added Successfully")
            path = request.get_full_path().rfind('/')
            if '&object' in request.get_full_path()[path:]:
                return redirect(request.get_full_path()[0:request.get_full_path().find('&object')])
            else:
                return redirect(request.get_full_path())
        else:
            messages.error  (request,"Plese Check Your Fields, Invalid Opration")
            li[page_number] = form
    sec = Sections.objects.filter(reg_title = RegistrationSubMenuob)
    sec = sectionname
    paginator = Paginator(li, 1)
    page_number = request.GET.get('page')
    res['page_obj'] = paginator.get_page(page_number)
    if isinstance(res['page_obj'].object_list[0],list):
        paginator2 = Paginator(res['page_obj'].object_list[0], 1)
        card = request.GET.get('card')
        res['card_obj'] = paginator2.get_page(card)
        if 'icon' in res['card_obj'].object_list[0].fields:
            res['icon'] = icon.objects.all()
    res['forms'] = li
    res['slugs'] = [slug1,slug2,RegistrationSubMenuob]
    res['sec'] = [[i,sec[i-1]] for i in res['page_obj'].paginator.page_range ]
    try:
        return render(request,f'{templateFolder}/extra/editregistraions.html',res)
    except Exception as e:    
        print(e)
        return render(request,'editregistraions.html',res)





def deleteregistration(request):

    if request.method == "POST":
        formid = int(request.POST.get('page') if request.POST.get('page') is not None and request.POST.get('page')!=""  else 1) - 1
        delid = request.POST.get('id')
        ret = request.POST.get('return')
        if ret is not None:
            data = sections[formid].objects.get(id=delid)
            data.delete()
            messages.error(request,"successfully deleted")
            return redirect(ret)
    return redirect(request.get_full_path()[0:request.get_full_path().find('&object')])
from chat.models import user,convofiles
def adminchat(request,slug1=None,id=None):
    res = {}
    if request.method=="POST":
        msg = request.POST['message']   
        files= request.FILES.get('myfile')
        convo=conversation(msgby = user.objects.get(user=id),msgtoadmin=False,msg=msg)
        convo.save()
        if files is not None:
            convofiles(msg=convo,file=files).save()
        return HttpResponse("{'msg':"+msg+"}")
    if id is not None:
        res['coverstion'] = conversation.objects.filter(msgby__user=id)
        res['window'] = True
        res['slug'] = [slug1,id]
        res['username'] = user.objects.get(user=id).user.username
    list = conversation.objects.values('msgby__user__id') 
    resp = []
    for i in list:
        if i not in resp:
            resp.append(i)
    res['chats'] = [[User.objects.get(id=i['msgby__user__id']),User.objects.get(id=i['msgby__user__id']).user.msgby.all().order_by('-time')] for i in resp]
    try:
        return render(request,f'{templateFolder}/extra/adminchat.html',res)
    except Exception:    
        return render(request,'adminchat.html',res)
def alluser(request):
    res = {}
    try:
        return render(request,f'{templateFolder}/extra/alluser.html',res)
    except Exception:    
        return render(request,'alluser.html',res)

def getmsg(request,slug1=None,id=None):
    auser = User.objects.get(id=id)
    mlen = request.GET.get('len')
    messages = list(conversation.objects.filter(msgby__user=auser.id).order_by('time').values('msgby__user',
'msgtoadmin','msg','convofiles__file'))
    if len(messages)==int(mlen):
        return HttpResponse("updated")
    return JsonResponse(messages[int(mlen):],safe=False)
def dashboardlogout(request):
    logout(request)
    return redirect('dindex')
from Home.models import *
from .homeforms import * 
homemodel = [Slider,aboutca,News,DueDateReminder,BlogNews,addblog]
homeform = [[sliderform],aboutcaform,[Newsform],[DueDateReminderform],[BlogNewsform],[addblogform]]
editname = ['slider','AboutCA','News_nortification','DueDate_Reminder','Blog_News_nortification','New_Blogs']
def edithome(request,slug=None):
    res={}
    res["title"] = "Edit home" if slug is None else "Edit "+ slug
    if slug is not None:
        res['slug'] = slug
        if slug in editname:
            d = editname.index(slug)
            if isinstance(homeform[d],list):
                data = homemodel[d].objects.all()
                res["forms"] = [homeform[d][0](instance=da) for da in data]
                res['forms'].append(homeform[d][0]())
            else:
                data = homemodel[d].objects.all()
                if data.exists():
                    data= data[0]
                else:
                    data=None
                res["forms"] = [homeform[d](instance=data)]
    if request.method == "POST":
        objectno = (request.GET.get('object') if request.GET.get('object') is not None else 1)
        if homeform[d] is None or objectno == "new":
            if isinstance(homeform[d],list):
                form = homeform[d][0](request.POST,request.FILES,instance = None)
            else:
                form = homeform[d](request.POST,request.FILES,instance = None)

        else:
            if isinstance(homeform[d],list):
                form = homeform[d][0](request.POST,request.FILES,instance = homemodel[d].objects.filter(id=objectno)[0])
            else:
                form = homeform[d](request.POST,request.FILES,instance = homemodel[d].objects.filter(id=objectno)[0])
        if form.is_valid():
            form.save()
            messages.success(request,"Information Is Added Successfully")
            return redirect(request.get_full_path()[0:request.get_full_path().find('&object')])
        else:
            messages.error  (request,"Plese Check Your Fields, Invalid Opration")
    try:
        return render(request,f'{templateFolder}/extra/dashboardhome.html',res)
    except Exception:    
        return render(request,'dashboardhome.html',res)
def deletehome(request,slug):
    if slug is not None:
        formid = editname.index(slug)
        if request.method == "POST":
            delid = request.POST.get('id')
            ret = request.POST.get('return')
            if ret is not None:
                data = homemodel[formid].objects.get(id=delid)
                data.delete()
                messages.error(request,"successfully deleted")
                return redirect(ret)
    return redirect(request.get_full_path()[0:request.get_full_path().find('&object')])
def viewicon(request):
    iconlist = icon.objects.all()
    try:
        return render(request,f'{templateFolder}/extra/iconpack.html',{'icon':iconlist})
    except Exception:    
        return render(request,'iconpack.html',{'icon':iconlist})
def contact(request):
    res = {}
    res['title'] = "Registration Contacts"
    res['contacts'] = contacts.objects.all().order_by('-time')
    try:
        return render(request,f'{templateFolder}/extra/drcontacts.html',res)
    except Exception:    
        return render(request,'drcontacts.html',res)
def delcontacts(request):
    if request.method=="POST":
        delval = request.POST['delval'].split(',')
        for d in delval:
            d = contacts.objects.filter(id=d)
            if d.exists():
                d[0].delete()
        messages.error(request,"contact Deleted successfully")
    return redirect('drcontact')
def clearchat(request,slug1=None,id=None):
    if slug1 is not None and id is not None:
        for d in conversation.objects.filter(msgby__user=id):
            d.delete()
    return redirect(request.get_full_path().replace('/clearchat/',''))
def setpayment(request,slug1=None,id=None):
    if slug1 is not None and id is not None and request.method=='POST':
        reason = request.POST['reason']
        Ammount = request.POST['Ammount']
        USER = User.objects.get(id=id)
        msg = "You Have to Pay " + Ammount + " for " + reason + " Click on Payment at Top Left Corner"
        if makepaymentrequest.objects.filter(user=USER.id,status="pending").exists():
            messages.error(request,"There is already a Pending payment request delete the payment request or Try again Later")
        else:
            makepaymentrequest(user=USER,reason=reason,ammount=Ammount).save()
            conversation(msgby =  user.objects.get(user=id),msgtoadmin=False,msg=msg).save()
            messages.success(request,"Payment request send successfully")
    return redirect(request.get_full_path().replace('/setpayment/',''))