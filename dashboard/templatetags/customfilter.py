from django import template
import random

register = template.Library()
@register.filter(name='rancolor')
def cut(value):
    r = lambda: random.randint(0,255)
    return '#%02X%02X%02X' % (r(),r(),r())