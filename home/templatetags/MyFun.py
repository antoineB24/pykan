from django import template
from ..urls import urlpatterns
from django.urls import resolve
from django.http import HttpRequest

register = template.Library()

@register.filter
def add(str1, str2):
    return str1 + str2

@register.filter
def dir_fun(obj):
    return dir(obj)

@register.simple_tag()
def include_url(url):
    http = HttpRequest()
    http.method = "GET"
    func, args, kwargs= resolve(url, urlconf=tuple(urlpatterns))
    return func(http, **kwargs).content.replace('\\n', '')