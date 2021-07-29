from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.conf import settings
from . import models
import string, random as rand
#import models

# Create your views here.

#n = open('Users\\antoine\\Documents\\pyforum\\pyforum\\home\\models.py');exec(n.read());n.close()

make_id = lambda n : ''.join([rand.choice(string.ascii_letters + '1234567890') for i in range(n)])
in_fun = lambda a, b : [a == i for i in b]

def get_(req, name):
    return req.POST.get(name)

def home(request):
    #
    n = open("data.dt", "r")
    user = n.read()
    
    n.close()
    obj = None
    if user:
        obj = models.Compte.objects.get(name=user)
        
    
    return render(request, "home.html", locals())

def login(request):
    


    if request.method == "POST":

        if request.POST.get('email') == '':
            return render(request, "login.html", locals())
        if request.POST.get('name') == '':
            return render(request, "login.html", locals())
        if len(models.Compte.objects.filter(name=request.POST.get('name'))) !=  1:
            return render(request, "login.html", locals())
        if request.POST.get('pass1') == '':
            return render(request, "login.html", locals())
        if models.Compte.objects.get(name=request.POST.get('name')).secrete != request.POST.get('pass1'):
            return render(request, "login.html", locals())


        n = open("data.dt", 'w');n.write(request.POST.get('name'));n.close()
        #print(compte.name)
        message = ("", True)
        #client.send(bytes(compte.name))
        return redirect("home")

    return render(request, "login.html", locals())

def signup(request):
    



    if request.method == "POST" :

        if get_(request, 'email') == '': 
             
            return render(request, "signup.html", locals())
        if get_(request, 'name') == '' or len(models.Compte.objects.filter(name=get_(request, 'name'))): return render(request, "signup.html", locals())
        if get_(request, 'pass1') == '' or get_(request, 'pass2') == '' or get_(request, 'pass1') != get_(request, 'pass2'): 
            return render(request, "signup.html", locals())


        pass1 = get_(request, 'pass1') #form.cleaned_data['pass_']
        name =  get_(request, 'name') #form.cleaned_data['name']
        pass2 = get_(request, 'pass2') #form.cleaned_data['pass2']
        email = get_(request, 'email')
        mess = ""
        inobj = False
        for obj in models.Compte.objects.all():
            if obj.name == name:
                inobj = True
        
        id_ = make_id(7)
        while any(in_fun(id_, models.Compte.objects.all())):
            id_ = make_id(7)
        

        q = open("data.dt", 'w');q.write(name);q.close()

        n = models.Compte(secrete=pass1, name=name, id_name=id_, email=email)
        n.save()
        return redirect('home')
        
            
    return render(request, "signup.html", locals())

def deconecte(request):
    open("data.dt", "w").close()

    return redirect('home')

def profil(request, idname):
    
    n=open('data.dt');user=n.read();n.close()
    err = False
    if not user:
        err = True
    obj = get_object_or_404(models.Compte, id_name=idname)
    #obj = models.Compte.objects.get(id_name=idname)
    user_co = False

    if(obj.name == user) :
        user_co = True
    image_input = models.get_ChangeImgage()(request.POST or None, request.FILES)
    
    if request.method == "POST":
        if image_input.is_valid():
            obj.img_profil = image_input.cleaned_data['image']
            obj.save()
        

    
    string_set_pass_cmd = "/home/profil/%s/set_pass" % idname

    return render(request, 'profil.html', locals())

def set_pass(request, idname):
    n=open('data.dt');user=n.read();n.close()
    obj = models.Compte.objects.get(name=user)
    user_co = True
    if obj.id_name != idname:
        user_co = False
    form = models.get_form_setPass(user)(request.POST or None)
    if form.is_valid():
        obj.secrete = form.cleaned_data['new_pass2']
        obj.save()
    return render(request, 'set_pass.html', locals())



