from django import template
from ..urls import urlpatterns
from django.urls import resolve, reverse

register = template.Library()



@register.simple_tag()
def include_url( request, url):
    urlpatterns_cp = tuple(urlpatterns)

    func, args, kwargs= resolve(reverse(url), urlconf=tuple(urlpatterns))
    return func(request, *args, **kwargs).content.replace('\\n', '')