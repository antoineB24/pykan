from posixpath import commonpath
import sys
from django import forms as form
sys.path.append('..')
from django.shortcuts import render
from django.http import HttpResponse
from .models import Messenger, MessengerForm
from home.models import Compte

# Create your views here.

def messenger(request):
    nb_no_read = 0
    n=open('data.dt');user=n.read();n.close()
    
    obj1 = Compte.objects.get(name=user)
    
    obj = Messenger.objects.filter(destinataire=user)
    for i in obj:
        if i.new:
            nb_no_read += 1

    return render(request, 'messenger.html', locals())


def send(request):
    n=open('data.dt');user=n.read();n.close()
    obj1 = Compte.objects.get(name=user)

    obj = Messenger.objects.filter(author=user)
    return render(request, 'send.html', locals())


def read(request):
    n=open('data.dt');user=n.read();n.close()
    obj1 = Compte.objects.get(name=user)
    obj = Messenger.objects.filter(destinataire=user)
    for i in obj:
        i.new = False 
        i.save()
    
    return render(request, 'read.html', locals())

def write(request):
    forms = MessengerForm(request.POST or None)
    n=open('data.dt');user=n.read();n.close()
    obj1 = Compte.objects.get(name=user)
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
            
            Messenger(author=user
                ,destinataire=forms.cleaned_data['destinataire']
                ,sujet=forms.cleaned_data['subject']
                ,body=forms.cleaned_data['body']
                ,new=True).save()
            send = True


    return render(request, 'write.html', locals())