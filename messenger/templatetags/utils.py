import sys 
sys.path.append("../../..")
from django import template 
from django.contrib.auth.models import User

register = template.Library()

@register.filter
def get_url_img(name):
    return User.objects.get(username=name).profil.img_profil.url
