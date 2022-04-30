import sys
sys.path.append('..')

from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from home.models import   Action, Profil
from django.contrib.auth.decorators import login_required
import random as r



mess = (False, "")
messErr = (False, "")

MyZip = lambda a,b: [(a[i], b[i]) for i in range(len(a))]
mk_id_b = lambda l: ''.join([r.choice('azertyuiopqsdfghjklmwxcvbn1234567890') for i in range(l)])

@login_required
def create_blog(request):
    mess = (False, "")
    user = request.user

    err = request.user.is_authenticated
    formblog = getBlogForm(user.username)(request.POST or None)
    if formblog.is_valid():
        if not mess[0]:

            Blog(name=formblog.cleaned_data['name'], author=user.username, body=formblog.cleaned_data['body'], idblog=mk_id_b(9)).save()
            return redirect(to='http://127.0.0.1:8000/blog/')

    return render(request, 'create_blog.html', locals())
def blog(request):    
    


    return render(request, "blog.html", locals())

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

def go_blog(request, idblog):
    blog = get_object_or_404(Blog, idblog=idblog)
    forumblog = ForumBlog.objects.filter(blog=blog)
    return render(request, 'go_blog.html', locals())

