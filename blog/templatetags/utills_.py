from django import template
from ..views import *
from django.http import HttpRequest, HttpResponse

register = template.Library()

@register.simple_tag
def _load_html(request_, name):
    
#\n
    if name == 'create_blog':
        return str(create_blog(request_).content).replace('\\n','')
    elif name == 'write_mess':
        return str(write_mess(request_).content).replace('\\n','')
    else:
        return 'RIEN'

@register.filter
def replace_char(a):
    return a.replace('\n', '<br/>')

@register.filter
def to_str(v):
    return str(v)