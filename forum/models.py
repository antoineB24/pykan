
from django.db import models
from django.db import *
from django.forms.forms import Form
from django.utils import timezone
from django import forms
import socket


#serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#serveur.connect(('localhost', 1234))



messErr = ("", False)


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


class ForumPrivateBody(models.Model):
    user = models.CharField(max_length=50)
    date = models.DateTimeField(default=timezone.now, verbose_name="date send message")
    mess = models.TextField(max_length=500)
    name_forum = models.CharField(max_length=50)

    class Meta:
        verbose_name= 'ForumPrivateBody'
        ordering = ['date']
    def __str__(self):
        return self.user

class ForumPrivate(models.Model):
    
    user = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    accept = models.CharField(max_length=200)
    date = models.DateTimeField(default=timezone.now, verbose_name="date created forum")
    id_forum = models.CharField(max_length=50, default='')
    class Meta:
        verbose_name= 'Forum Private'
        ordering= ['date']
    def __str__(self):
        return self.title

def getForumForm(name):
    class ForumForm(forms.Form):
        author = forms.CharField(max_length=50,initial=name, disabled=True)
        mess = forms.CharField(max_length=500, widget=forms.Textarea(), required=True, label="message ")
    return ForumForm



def getNewForumPrivateForm(user):
    list_amie = ['choose a amie'] + [i for i in user.profil.amie.split('#') if i]
    class NewForumPrivateForm(forms.Form):
        accept = forms.CharField(max_length=10, required=False, label='l\' id name de la personne')
        title = forms.CharField(max_length=50, required=True)
        max_message = forms.IntegerField(max_value=5000, required=True, min_value=0)
    return NewForumPrivateForm

def getForumPrivateBodyForm(user):
    class ForumPrivateBodyForm(models.Model):
        author = forms.CharField(max_length=50,initial=user.username, disabled=True)
        mess = forms.CharField(max_length=500, widget=forms.Textarea(), required=True, label="message ")
    return ForumPrivateBodyForm






