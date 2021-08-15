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

# Create your views here.
def index(request):
    res = {}
    res["title"] = "Dashboard"
    return render(request,'dashboard.html',res)
def registration(request,slug=None):
    res = {}
    if slug is not None:
        res['registration'] = Registration.objects.filter(slug=slug)
    else:
        res['registration'] = Registration.objects.all()
    res["title"] = "Registration"
    return render(request,'dregistrations.html',res)

sections = [SubRegistrationContent,AboutRegistraionSubMenu,DocumentRequired,PackageIncluded,Procedure,Memorandum,CompanyRegisterRequirements,FAQ,Sainification,ourclients]
# adding multi objects form as a list in sectionsform
sectionsforms = [section0Form,section1Form,section2Form,[PackageIncludedForm],[section3Form],section4Form,section5Form,[section6Form],section7Form,[section8Form]]

def editregistration(request,slug1,slug2):
    RegistrationSubMenuob = RegistrationSubMenu.objects.get(slug=slug2,title__slug=slug1)
    s = []
    for i in sections:
        s.append(i.objects.filter(reg_title = RegistrationSubMenuob) if i.objects.filter(reg_title = RegistrationSubMenuob).exists() else [None] )
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
            form.save()
            messages.success(request,"Information Is Added Successfully")
            return redirect(request.get_full_path()[0:request.get_full_path().find('&object')])
        else:
            messages.error  (request,"Plese Check Your Fields, Invalid Opration")
            li[page_number] = form
    sec = Sections.objects.filter(reg_title = RegistrationSubMenuob)
    if sec.exists():
        sec = json.loads(sec[0].section)
    else:
        sec = Sections(reg_title=RegistrationSubMenuob)
        sec.save()
        sec = json.loads(sec.section)
    paginator = Paginator(li, 1)
    page_number = request.GET.get('page')
    res['page_obj'] = paginator.get_page(page_number)
    if isinstance(res['page_obj'].object_list[0],list):
        paginator2 = Paginator(res['page_obj'].object_list[0], 1)
        card = request.GET.get('card')
        res['card_obj'] = paginator2.get_page(card)
    res['forms'] = li
    res['slugs'] = [slug1,slug2,RegistrationSubMenuob]
    res['sec'] = [[i,sec[i-1]] for i in res['page_obj'].paginator.page_range ]
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
from chat.models import user
def adminchat(request,slug1=None,id=None):
    res = {}
    if request.method=="POST":
        msg = request.POST['message']   
        conversation(msgby = user.objects.get(user=id),msgtoadmin=False,msg=msg).save()
        return HttpResponse("{'msg':"+msg+"}")
    if id is not None:
        res['coverstion'] = conversation.objects.filter(msgby__user=id)
        res['window'] = True
        res['slug'] = [slug1,id]
    res['chats'] = User.objects.filter(is_superuser=False)
    return render(request,'adminchat.html',res)
def getmsg(request,slug1=None,id=None):
    auser = User.objects.get(id=id)
    mlen = request.GET.get('len')
    messages = list(conversation.objects.filter(msgby__user=auser.id).order_by('time').values('msgby__user',
'msgtoadmin','msg'))
    if len(messages)==int(mlen):
        return HttpResponse("updated")
    return JsonResponse(messages[int(mlen):],safe=False)
