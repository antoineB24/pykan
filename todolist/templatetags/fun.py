from django.template import Library

register = Library()

@register.simple_tag
def use_fun(f, *args, **kwargs):
    return f(*args, **kwargs)
