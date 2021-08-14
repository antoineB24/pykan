import sys
from django import forms as form
sys.path.append('..')
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Messenger, MessengerForm
from home.models import  Action, Profil
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def messenger(request):
    user = request.user
    nb_no_read = 0
    
    co = user.is_authenticated

    if co:
        obj1 = user.profil
    
        obj = Messenger.objects.filter(destinataire=user.username)
        for i in obj:
            if i.new:
                nb_no_read += 1

    return render(request, 'messenger.html', locals())


def send(request):
    user = request.user
    co = user.is_authenticated
    if co:
        obj1 = user.profil

        obj = Messenger.objects.filter(author=user.username)
    return render(request, 'send.html', locals())


def read(request):
    user = request.user
    co = user.is_authenticated
    if co:
        obj1 = user.profil
        obj = Messenger.objects.filter(destinataire=user.username)
        for i in obj:
            i.new = False 
            i.save()
    
    return render(request, 'read.html', locals())

def write(request):
    forms = MessengerForm(request.POST or None)
    user = request.user
    co = user.is_authenticated

    
    if co:
        obj1 = user.profil
        send = False
        if forms.is_valid():
            send = False
            correct = True
            try: 
                Compte.objects.get(name=user)
            except:
                print("ERREUR")
                correct = False
            if correct:
                Action(
                    title=forms.cleaned_data['subject'],
                    from_app='messenger',
                    user=user.username,
                    body='vous avez envoyé un message à %s' % forms.cleaned_data['destinataire']
                    ).save()
                Messenger(author=user.username
                    ,destinataire=forms.cleaned_data['destinataire']
                    ,sujet=forms.cleaned_data['subject']
                    ,body=forms.cleaned_data['body']
                    ,new=True).save()
                send = True


    return render(request, 'write.html', locals())

def view(request, id):
    obj = get_object_or_404(Messenger, id=id)
    return render(request, 'view.html', locals())