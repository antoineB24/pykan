import sys
sys.path.append('..')

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from home.models import   Action, Profil
from django.contrib.auth.models import User


mess = (False, "")
messErr = (False, "")

MyZip = lambda a,b: [(a[i], b[i]) for i in range(len(a))]

def create_blog(request):
    mess = (False, "")
    user = request.user
    if not user.is_authenticated:
        mess = (True, "Erreur: Vous ne pouvez pas écrire sans vous connectez")
    obj1 = user.profil
    formblog = getBlogForm(user.username)(request.POST or None)
    if formblog.is_valid():
        if not mess[0]:
            Action(
                title=formblog.cleaned_data['name'],
                from_app='blog',
                user=user.username,
                body=f'''vous avez crée le blog {formblog.cleaned_data['name']}''').save()
            Blog(name=formblog.cleaned_data['name'], author=user.usernames, body=formblog.cleaned_data['body']).save()
            return redirect(to='http://127.0.0.1:8000/blog/')

    return render(request, 'create_blog.html', locals())
def blog(request):    
    user = request.user
    if user.is_authenticated:
        obj = user.profil
        idname = obj.id_name
    else:
        err = True
    body_blog = Blog.objects.all()
    
    body_blog_forum = ForumBlog.blog
    
    range1 = Blog.objects.all()
    range2 = ForumBlog.objects.all()

    local = locals()
    local.update({'mess': mess})
    local.update({'messErr': messErr})
    return render(request, "blog.html", {**locals(), **globals()})

def write_mess(request):
    user = request.user
    formblogforum = getForumBlogForm(user.username)(request.POST or None)
    if formblogforum.is_valid():
        try :
            Blog.objects.get(name=formblogforum.cleaned_data['blog'])
        except Blog.DoesNotExist: 
            messErr = (True, "Pas De Nom ")
        else:
            Action(
                title='Forum_blog',
                from_app='blog_forum',
                user=user.username,
                body=f'''vous avez commenté le blog '{formblogforum.cleaned_data['blog']}' ''').save()
            ForumBlog(author=user, body=formblogforum.cleaned_data['body'], blog=Blog.objects.get(name=formblogforum.cleaned_data['blog'])).save()
            return redirect(to='http://127.0.0.1:8000/blog/')
    return render(request, 'write_mess.html', locals())

