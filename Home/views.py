from django.contrib.auth.backends import RemoteUserBackend
from chat.models import conversation, user
from dashboard.homeforms import aboutcaform
from django.contrib import messages
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from . models import *
from registration.models import *
from taxfiling.models import *
from django.contrib.auth import authenticate, login, logout
MERCHANT_KEY='ey1DQFRPXypAmeE3'


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
    client = ourclients.objects.all()[:3]
    res = { 
        'slider':slider,
        "aboutca":abca ,
        'news':news,
        'ddreminder':ddreminder,
        'bnews':bnews,
        'offrings':offrings,
        'menu':menu,
        'latestblog': latestblog,
        'client':client
    }
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        data = BusinessQuery(name=name, email=email, phone=phone, message=message)
        data.save()
        messages.success(request,"Hurrey! Thanks For Contacting With us, We will Get Back To You Soon.")
        return redirect('index')
    return render(request,'index.html',res)

def about(request):
    res= {}
    res["banner"]= headbanner.objects.all()[0]
    res["links"]= links.objects.all()
    res["exper"]= Expertise.objects.all()
    res["marketplace"]= marketplace.objects.all()
    res['content'] = aboutContent.objects.all()
    return render(request,'about.html',res)

def another(request):
    return render(request,'another.html')

def blogpage(request):
    return render(request,'blog-page.html')



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
                return JsonResponse({'status':'ok','msg':'Login Success'})
            return JsonResponse({"status":'invaliduser','msg':'invalid user'})
    return render(request,'logindashboard.html')
from django.contrib.auth.decorators import login_required
from dashboard.models import makepaymentrequest
from paytm import Checksum
@login_required(login_url='memberlogin')
def payment(request):
    pendingpayments = makepaymentrequest.objects.filter(user=request.user.id,status="pending")
    if pendingpayments.exists():
        order = OrderPlaced.objects.create(user=request.user,payreq = pendingpayments[0],ammount=pendingpayments[0].ammount )
        order.save()
        paytmParams={

            'MID': 'yUvqPZ56033952526905',
            'ORDER_ID': str(order.order_id),
            'TXN_AMOUNT': str(pendingpayments[0].ammount),
            'CUST_ID': request.user.email,
            'INDUSTRY_TYPE_ID': 'Retail',
            'WEBSITE': 'WEBSTAGING',
            'CHANNEL_ID': 'WEB',
            'CALLBACK_URL':'http://'+request.get_host()+'/handlerequest/',
        }
        paytmParams["CHECKSUMHASH"] = Checksum.generateSignature(paytmParams, "ey1DQFRPXypAmeE3")
        print(paytmParams)
        return render(request,'payttm.html',{'dic':paytmParams})
        # print(paytmParams)
    else:
        messages.error(request,"You Don't Have Any Payment Request ! Please Contact on Chat")
        return redirect("index")
from django.views.decorators.csrf import csrf_exempt
import json
@csrf_exempt
def handelrequest(request):
    if request.method == "POST":
        resp = request.POST
        print(resp)
        param = {}
        OrderPlaced.objects.filter(order_id=resp["ORDERID"]).update(other_data=json.dumps(resp));
        for data in resp:
            param[data] = resp[data]
        if Checksum.verifySignature(param ,'ey1DQFRPXypAmeE3',resp['CHECKSUMHASH']):
            if resp['RESPCODE'] == '01':
                OrderPlaced.objects.filter(order_id=resp["ORDERID"]).update(status="Success");
                mpr = makepaymentrequest.objects.get(id=OrderPlaced.objects.get(order_id=resp["ORDERID"]).payreq.id)
                mpr.status = "success"
                mpr.save()
                msg = "the payment of" + str(mpr.ammount) + " for " + mpr.reason + " is done " + " TXNID is " + str(resp['ORDERID'])
                conversation(msgby =  user.objects.get(user=OrderPlaced.objects.get(order_id=resp["ORDERID"]).user),msgtoadmin=True,msg=msg).save()
                messages.success(request,"Your Payment is Successfull")
            else:
                messages.success(request,"Your Payment is unsuccessfull because "+resp['RESPMSG'] )

        return redirect('index')
    return redirect('index')
def services(request):
    return render(request,'services.html')


# profile sections
from .forms import Userform,userform
@login_required(login_url='memberlogin')
def profile(request):
    res= {}
    res['title'] = "Profile"
    return render(request,'profile.html',res)

@login_required(login_url='memberlogin')
def bookings(request):
    res= {}
    res['title'] = "Profile"
    res['booking'] = OrderPlaced.objects.filter(user=request.user.id)
    return render(request,'bookings.html',res)
@login_required(login_url='memberlogin')
def documents(request):
    if request.method == "POST":
        name = request.POST['docname']
        document = request.FILES['document']
        documents(user=request.user,name=name,doc=document).save()
        messages.success(request,name +' Uploaded Successfully')
        return redirect('documents')
    res= {}
    res['title'] = "Documents"
    res['document'] = documents.objects.filter(user=request.user.id)
    return render(request,'documents.html',res)
@login_required(login_url='memberlogin')
def getdoclist(request):
    value = request.GET.get('doc')
    if value is not None:
        data = documents.objects.filter(name__contains=value).values('name')
        data={item['name'] for item in data}
        data = json.dumps(list(data))
        return HttpResponse(data)
    return HttpResponse('hello')
@login_required(login_url='memberlogin')
def editprofile(request):
    res = {}
    Uform = Userform(instance = request.user)
    uform = userform(instance = request.user.user)
    if request.method == "POST":
        Uform = Userform(request.POST,instance = request.user)
        uform = userform(request.POST,request.FILES,instance = request.user.user)
        if Uform.is_valid and uform.is_valid:
            uform.save()
            Uform.save()
            messages.success(request,'Your Profile Is Updated')
            return redirect('editprofile')
        else:
            messages.error(request,"Invalid data")
    res['form'] = [Uform,uform]
    return render(request,'editprofile.html',res)
@login_required(login_url='memberlogin')
def changepass(request):
    return render(request,'changepass.html')



# resourses sections
def getblog(request,res,id):
    res['blogob'] = BlogNews.objects.get(id=id)
    res['recentblog'] = BlogNews.objects.all().order_by('-date')[:4]
    res['title'] = res['blogob'].title
    current = res['blogs'].filter(id__lt = res['blogob'].id).count()
    print(current)
    res['nextblog'] = res['blogs'][current+1] if len(res['blogs'])-1 > current else False
    res['prevblog'] = res['blogs'][current-1] if current > 0 else False
    return render(request, 'blogdetails.html',res)
def blog(request,id=None):
    type = "blog"
    res= {}
    res['blogs'] = BlogNews.objects.filter(type='2')      
    res['title'] = "Blogs"
    res['type'] = type
    res['pageurl'] = 'singleblog'
    if id is not None:
        return getblog(request,res,id)
    return render(request,'blog.html',res)
def news(request,id=None):
    type = "news"
    res= {}
    res['title'] = "News"
    res['type'] = type
    res['pageurl'] = 'singlenews'
    res['blogs'] = BlogNews.objects.filter(type='1')      
    if id is not None:
        return getblog(request,res,id)
    return render(request,'blog.html',res)