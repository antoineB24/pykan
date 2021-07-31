import sys
sys.path.append('..')
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from home.models import Compte, Action

# Create your views here.
def forum(request):
    #if messErr[1]:
      #  err = True
    #@  return render(request, "forum.html", locals())
    n = open('data.dt');user=n.read();n.close()
    err = ""
    if not bool(user):
        err = "Erreur: Vous ne pouvez pas écrire sans vous connectez"


    forum_form = getForumForm(user)(request.POST or None)
    
    
    if forum_form.is_valid():
        
        author = forum_form.cleaned_data['author']
        data = open('data.dt')
        author = data.read()
        mess = forum_form.cleaned_data['mess']
        data.close()
        Action(
            title='Forum',
            from_app='forum',
            user=user,
            body="vous avez posté un message"
            ).save()
        Forum(user=author, mess=mess).save()

    forum = Forum.objects.all()
    c = Compte.objects
    if not err:
        obj = c.get(name=user)
        

    
        idname = obj.id_name
    

    return render(request, "forum.html", locals())

def list_forum(request):
    pass