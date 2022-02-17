import imp
from django import template
import random
from registration.models import icon
from Home.models import ContactDetails

register = template.Library()
@register.filter(name='rancolor')
def cut(value):
    r = lambda: random.randint(0,255)
    return '#%02X%02X%02X' % (r(),r(),r())
@register.filter(name='geticon')
def geticon(value):
    data = value.split(' ')
    print(data)
    iconlist = icon.objects.all()
    for d in data:
        iconli = iconlist.filter(icon__contains = d)
        if iconli.exists():
            return iconli[0].icon
    return iconlist[random.randint(0,len(iconlist)-1)]
from django import template
from dashboard.dashboardsettings import appslist,appmodels

@register.filter(name='sidebardata')
def sidebardata(value):
    return appmodels(appslist)
@register.filter(name='cemelcase')
def cemelcase(value):
    res = ''
    count = 0
    for s in str(value):
        if count != 0 and s == s.upper():
            s = " "+s
        res+=s
        count+=1
    return res
@register.filter(name='getattribute')
def getattribute(value,arg):
    try:    
        data = getattr(value , arg)
        if len(str(data))>0:
            return data
        else:
            return "-"
    except Exception as e:
        return "-"
@register.filter(name='split')
def splitdata(value,args):
    return value.split(args)
@register.filter(name="getpercent")
def getpercent(value,arg):
    value = float(value)
    arg = float(arg)
    percent = (arg*100)/value
    return str(percent)[:5]
@register.filter(name="showrelated")
def showrelated(value,args):
    return "showing related"

@register.filter(name="contact")
def getcontact(value):
    return ContactDetails.objects.all()