from django import template
import random
from registration.models import icon

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
