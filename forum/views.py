import sys
sys.path.append('..')
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from home.models import  Action, Profil
from django.contrib.auth.models import User

# Create your views here.
def forum(request):
    #if messErr[1]:
      #  err = True
    #@  return render(request, "forum.html", locals())
    user = request.user
    err = ""
    if not user.is_authenticated:
        err = "Erreur: Vous ne pouvez pas écrire sans vous connectez"


    forum_form = getForumForm(user.username)(request.POST or None)
    
    
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
    if not err:
        obj = c.get(username=user.username)
        

    
        idname = obj.profil.id_name
    

    return render(request, "forum.html", locals())

def list_forum(request):
    pass