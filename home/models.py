from os import name
from django.db import models
from django.utils import timezone
from django.shortcuts import redirect, render

import time

# Create your models here.
from django import forms

USER = ''
USER_PASS = ''

class Login(forms.Form):
    name = forms.CharField(max_length=50)
    pass_ = forms.CharField(max_length=50, widget=forms.PasswordInput)
    
class Signup(forms.Form):
    name = forms.CharField(max_length=50)
    pass_ = forms.CharField(max_length=50, widget=forms.PasswordInput)
    pass2 = forms.CharField(max_length=50, widget=forms.PasswordInput)
    def clean_pass2(self):
        
        if self.cleaned_data['pass_'] != self.cleaned_data['pass2']:
            raise forms.ValidationError("votre pass doit être identique: %s" % self.cleaned_data['pass_'])
        
        return self.cleaned_data['pass2']
    '''def is_valid(self) :
        return self.cleaned_data['pass_'] != self.cleaned_data['pass2'] and super().is_valid()
'''

class Compte(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateTimeField(default=timezone.now, verbose_name="Date Sign Up")
    secrete = models.CharField(max_length=30)
    img_profil = models.ImageField(upload_to="photos/", \
        default='photos/default_img.png')
    id_name = models.CharField(max_length=10)

    class Meta:
        verbose_name = 'compte'
        ordering = ['date']
    def __str__(self) -> str:
        return self.name


    

def recup_data_signup(request):
    if request.method == 'POST':
        form = Signup(request.POST or None)

        mess = ""
        pass1 = request.POST.get("pass_")
        pass2 = request.POST.get("pass2")
        print("hello")
        name = request.POST.get("name")
        if pass1 != pass2:
            mess = "erreur"
        return (form, (pass1, pass2, name), mess)
    else:
        return (Signup(request.POST or None), (None, None, None), "")
        
    

def lire(user):
    try:
        compte = Compte.objects.get(name=user)
    except Compte.DoesNotExist:
        return None
    return compte
    

def recup_data_login(login):
    if login.is_valid():
        compte = lire(login.cleaned_data['name'])
        if not bool(compte):
            return False
        if compte.secrete != login.cleaned_data['pass_']:
            return False
        return compte
    else:
        return False

def get_form_setPass(user):
    class SetPassword(forms.Form):
        pass_ = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput)
        new_pass1 = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput)
        new_pass2 = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput)
        def clean_pass_(self):
            pass_c = self.cleaned_data['pass_']
            if Compte.objects.get(name=user).secrete != pass_c:
                raise forms.ValidationError('mot de pass invalide')
            return pass_c
        
        def clean_new_pass2(self):
            pass1 = self.cleaned_data['new_pass1']
            pass2 = self.cleaned_data['new_pass2']
            if pass1 != pass2:
                raise forms.ValidationError('mot de pass différent')
            return pass2
    return SetPassword

def get_ChangeImgage():
    class ChangeImage(forms.Form):
        image = forms.ImageField(required=False)
    return ChangeImage
