from typing import Pattern
from django.forms.widgets import NullBooleanSelect
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

mess = (False, "")
messErr = (False, "")

MyZip = lambda a,b: [(a[i], b[i]) for i in range(len(a))]

def create_blog(request):
    mess = (False, "")
    n=open('data.dt');user=n.read();n.close()
    if not bool(user):
        mess = (True, "Erreur: Vous ne pouvez pas écrire sans vous connectez")
    formblog = getBlogForm(user)(request.POST or None)
    if formblog.is_valid():
        if not mess[0]:
            Blog(name=formblog.cleaned_data['name'], author=user, body=formblog.cleaned_data['body']).save()
            return redirect(to='http://127.0.0.1:8000/blog/')

    return render(request, 'create_blog.html', locals())
def blog(request):    
    body_blog = Blog.objects.all()
    
    body_blog_forum = ForumBlog.blog
    
    range1 = Blog.objects.all()
    range2 = ForumBlog.objects.all()
    print(Blog.objects.all())
    local = locals()
    local.update({'mess': mess})
    local.update({'messErr': messErr})
    return render(request, "blog.html", {**locals(), **globals()})

def write_mess(request):
    n=open('data.dt');user=n.read();n.close()
    formblogforum = getForumBlogForm(user)(request.POST or None)
    if formblogforum.is_valid():
        try :
            Blog.objects.get(name=formblogforum.cleaned_data['blog'])
        except Blog.DoesNotExist: 
            messErr = (True, "Pas De Nom ")
        else:
            ForumBlog(author=user, body=formblogforum.cleaned_data['body'], blog=Blog.objects.get(name=formblogforum.cleaned_data['blog'])).save()
            return redirect(to='http://127.0.0.1:8000/blog/')
    return render(request, 'write_mess.html', locals())

