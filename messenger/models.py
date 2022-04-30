
from django.db import models
from django.utils import timezone
from django import forms


# Create your models here.

class Messenger(models.Model):
    author = models.CharField(max_length=50)
    destinataire = models.CharField(max_length=50)
    sujet = models.CharField(max_length=50)
    body = models.TextField(max_length=1000)
    new = models.BooleanField(default=False)
    date = models.DateTimeField(default=timezone.now, verbose_name='date')
    draft =  models.BooleanField(default=False)
    started = models.BooleanField(default=False)


    class Meta:
        verbose_name = 'Messenger'
        ordering = ['date']
    
    def __str__(self):
        return self.body

class GroupMsg(models.Model):
    messages = models.ManyToManyField(Messenger)
    date = models.DateTimeField(default=timezone.now)
    destinataire = models.CharField(max_length=50, default='')
    author = models.CharField(max_length=50, default='')
    subject=models.CharField(max_length=50, default='')

    class Meta:
        verbose_name = 'Group Msg'
        ordering=['date']
    def __str__(self) -> str:
        return str(self.date)



class MessengerForm(forms.Form):
    destinataire = forms.CharField(max_length=50, required=True)
    subject = forms.CharField(max_length=50, required=True)
    body = forms.CharField(max_length=1000, widget=forms.Textarea, required=True)


