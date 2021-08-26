import sys
sys.path.append('..')
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *
from home.models import  Action, Profil
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
import string, random as rand

# Create your views here.


make_id = lambda n : ''.join([rand.choice(string.ascii_letters + '1234567890') for i in range(n)])
def forum(request):
    #if messErr[1]:
      #  err = True
    #@  return render(request, "forum.html", locals())
    user = request.user
    err = ""
    if not user.is_authenticated:
        err = "Erreur: Vous ne pouvez pas écrire sans vous connectez"


    forum_form = getForumForm(user.username)(request.POST or None)
    #forum_private_form = getNewForumPrivateForm(request.user)(request.POST or None)
    
    
    if forum_form.is_valid():
        
        author = forum_form.cleaned_data['author']
        author = user.username
        mess = forum_form.cleaned_data['mess']
        Action(
            title='Forum',
            from_app='forum',
            user=user,
            body="vous avez posté un message"
            ).save()
        Forum(user=author, mess=mess).save()

    forum = Forum.objects.all()
    c = User.objects
    forum_private = ForumPrivate.objects.all()
    if not err:
        obj = c.get(username=user.username)
        list_amie_ = [i for i in user.profil.amie.split('#') if i]
        list_amie = []
        for i in User.objects.all():
            if i.username in list_amie_:
                list_amie.append(i)

        

    
        idname = obj.profil.id_name
    '''
    if forum_private_form.is_valid():

        liste = []
        for n in User.objects.all():
            if n.is_staff:
                continue
            liste.append(n.profil.id_name)
        if forum_private_form.cleaned_data['accept'] not in liste:
            return render(request, "forum.html", locals())
        ForumPrivate(
         user=user.username,
         title=forum_private_form.cleaned_data['title'],
         accept=forum_private_form.cleaned_data['accept'] + '#' + request.user.username,
         id_forum=make_id(6)
         ).save()

'''

    return render(request, "forum.html", locals())

def list_forum(request):
    pass

@login_required
def private_forum(request, idname):
    obj = request.user
    obj1 = get_object_or_404(ForumPrivate, id_forum=idname)
    if request.user.username not in obj1.accept.split('#'):
        return HttpResponseForbidden("vous n'avez pas le droit d'accéder a ce forum privée")
    form = getForumPrivateBodyForm(request.user)(request.POST or None)
    #print(form)
    return render(request, "forum_private.html", locals())
