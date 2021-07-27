import sys
#sys.path.append('../home')
from django.db import models
from django.utils import timezone
from django import forms


# Create your models here.

f=open('data.dt');user=f.read();f.close();del f
mess = (False , "")
if not bool(user):
    mess = (True, "vous devez vous connectez")

class Messenger(models.Model):
    author = models.CharField(max_length=50)
    destinataire = models.CharField(max_length=50)
    sujet = models.CharField(max_length=50)
    body = models.TextField(max_length=1000)
    new = models.BooleanField(default=False)
    date = models.DateTimeField(default=timezone.now, verbose_name='date')

    class Meta:
        verbose_name = 'Messenger'
        ordering = ['date']
    
    def __str__(self):
        return self.body

class MessengerForm(forms.Form):
    destinataire = forms.CharField(max_length=50, required=True)
    subject = forms.CharField(max_length=50, required=True)
    body = forms.CharField(max_length=1000, widget=forms.Textarea, required=True)
