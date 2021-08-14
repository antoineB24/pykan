from django import template
from ..urls import urlpatterns
from django.urls import resolve ,reverse

register = template.Library()

@register.filter
def add(str1, str2):
    return str1 + str2

@register.filter
def dir_fun(obj):
    return dir(obj)

@register.simple_tag()
def include_url(url, request):

    func, args, kwargs= resolve(url, urlconf=tuple(urlpatterns))
    return func(request, **kwargs).content.replace('\\n', '')