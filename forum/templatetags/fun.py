from os import name
from django import template

register = template.Library()

@register.simple_tag
def get_url(user, compte):
    obj = compte.get(name=user)
    return 'http://127.0.0.1:8000/home/profil/' + obj.id_name

@register.simple_tag
def get_img(user, compte):
    obj = compte.get(name=user)
    return obj.img_profil.url

    

@register.filter
def to_bool(var):
    return bool(var)