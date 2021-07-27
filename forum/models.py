from django.db import models
from django.db import *
from django.forms.forms import Form
from django.utils import timezone
from django import forms
import socket


#serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#serveur.connect(('localhost', 1234))

code = open("data.dt")
USER = code.read()
code.close()

login = not bool(USER)

messErr = ("", False)
print("hello tous le monde")

#exec()


# Create your models here.

class Forum(models.Model):
    user = models.CharField(max_length=50)
    date = models.DateTimeField(default=timezone.now, verbose_name="date send message")
    mess = models.TextField(max_length=500)

    class Meta:
        ordering = ['date']
        verbose_name = 'forum'
    
    def __str__(self) -> str:
        return self.mess

def getForumForm(name):
    class ForumForm(forms.Form):
        author = forms.CharField(max_length=50,initial=name, disabled=True)
        mess = forms.CharField(max_length=500, widget=forms.Textarea(), required=True, label="message ")
    return ForumForm
if login:
    messErr = ("ERREUR: Vous n'êtes pas connecté", True)




