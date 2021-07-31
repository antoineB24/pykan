import sys
sys.path.append('..')
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.conf import settings
from . import models
import string, random as rand
import re
from messenger.models import Messenger
from .models import Action, Notif
from django.utils import timezone
from forum.models import Forum
from blog.models import Blog, ForumBlog
#import models

# Create your views here.

#n = open('Users\\antoine\\Documents\\pyforum\\pyforum\\home\\models.py');exec(n.read());n.close()

make_id = lambda n : ''.join([rand.choice(string.ascii_letters + '1234567890') for i in range(n)])
in_fun = lambda a, b : [a == i for i in b]

def get_(req, name):
    return req.POST.get(name)

def isset(name):
    try:
        exec(name)

    except:
        return False
    else:
        return True



def home(request):
    #
    n = open("data.dt", "r")
    user = n.read()
    
    n.close()
    obj = None
    if user:
        obj = models.Compte.objects.get(name=user)
        list_a = Action.objects.filter(user=user).order_by('-date')
        notif = Messenger.objects.filter(destinataire=user, new=True).count()
        notif_ = Messenger.objects.filter(destinataire=user)
        a = Notif.objects.filter(from_app='messenger')
        for i in a:
            i.delete()
        for i in notif_:

            Notif(title=f"{i.sujet}", from_app='messenger', body=f'tu as recu un message de {i.author} à {i.date}', user=user).save()
        list_m = Messenger.objects.all()
        notif_l = Notif.objects.filter(user=user).order_by('-date')
        f = Forum.objects.order_by('date')[:5]
        b = Blog.objects.order_by('date')[:5]
        b_f = ForumBlog.objects.order_by('date')[:5]
        l_forum = Notif.objects.filter(from_app='forum', user=user)
        l_blog = Notif.objects.filter(from_app='blog', user=user)
        l_blog_forum = Notif.objects.filter(from_app='blog_forum', user=user)
        for q in l_forum:
            q.delete()
        for q in l_blog:
            q.delete()

        for i in f:
            if i.user == user:
                continue
            Notif(title='Forum', from_app='forum', user=user, body=f'{i.user} a posté un message').save()
        for i in b:
            if i.author == user:
                continue
            Notif(title=i.name, from_app='blog', user=user, body=f'le Blog {i.name} a été créer par {i.author}').save()
        
        

    

    
    return render(request, "home.html", locals())

def login(request):
    name_err = {
        'name' : {},
        'pass1': {}
        }

    value_name = ''
    value_pass1 = ''

    if request.method == "POST":
        


        if request.POST.get('name') == '':
            name_err['name']['mess'] = 'il faut le champ name'
            name_err['name']['err'] = 'invalid'
            return render(request, "login.html", locals())
        if len(models.Compte.objects.filter(name=request.POST.get('name'))) != 1:
            value_name = request.POST.get('name')
            name_err['name']['mess'] = 'nom introuvable'
            name_err['name']['err'] = 'invalid'
            return render(request, "login.html", locals())
        if request.POST.get('pass1') == '':
            
            name_err['name']['mess'] = 'Good'
            name_err['name']['err'] = 'valid'
            value_name = request.POST.get('name')
            name_err['pass1']['mess'] = 'il faut le champ pass1'
            name_err['pass1']['err'] = 'invalid'
            return render(request, "login.html", locals())
        if models.Compte.objects.get(name=request.POST.get('name')).secrete != request.POST.get('pass1'):
            value_pass1 = request.POST.get('pass1')
            value_name = request.POST.get('name')
            name_err['name']['mess'] = 'Good'
            name_err['name']['err'] = 'valid'
            name_err['pass1']['mess'] = 'pass invalid'
            name_err['pass1']['err'] = 'invalid'
            return render(request, "login.html", locals())


        n = open("data.dt", 'w');n.write(request.POST.get('name'));n.close()
        Action(title='Log In', from_app='home', body=f'tu t"est connecté', user=request.POST.get('name')).save()
        #print(compte.name)
        message = ("", True)
        #client.send(bytes(compte.name))
        return redirect('home')
        

    return render(request, "login.html", locals())
def signup(request):
    name_err = {
        'email' : {}, 
        'name_' : {},
        'pass1' : {},
        'pass2' : {}
        }
    value_email = ''
    value_name_ = ''
    value_pass1 = ''
    value_pass2 = ''
    dict_ = {}
    
    start_email = True

    if request.method == "POST" :
        
        if get_(request, 'email') == '': 
            name_err['email']['mess'] =  'il faut le champ email'
            name_err['email']['err'] = 'invalid'
            start_email = False
            return render(request, "signup.html", {**locals()})
        if not re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', get_(request, 'email')):
            name_err['email']['mess'] =  'champ email invalid'
            name_err['email']['err'] = 'invalid'
            start_email = False
            return render(request, "signup.html", {**locals()})
        if get_(request, 'name_') == '' :
            start_email = False
            name_err['email']['mess'] = 'Good'
            name_err['email']['err'] = 'valid'
            value_email = get_(request, 'email')
            name_err['name_']['mess'] = 'Il faut le champ name'
            name_err['name_']['err'] = 'invalid'

            return render(request, "signup.html", locals())
        if models.Compte.objects.filter(name=get_(request, 'name_')).count() > 0:
            name_err['email']['mess'] = 'Good'
            name_err['email']['err'] = 'valid'
            value_email = get_(request, 'email')
            value_name_ = get_(request, 'name_')
            name_err['name_']['mess'] = 'nom déja utilisé'
            name_err['name_']['err'] = 'invalid'
            return render(request, "signup.html", locals())
        
        if get_(request, 'pass1') == '' : 
            name_err['email']['mess'] = 'Good'
            name_err['email']['err'] = 'valid'
            value_email = get_(request, 'email')
            name_err['name_']['mess'] = 'Good'
            name_err['name_']['err'] = 'valid'
            value_name_ = get_(request, 'name_')
            name_err['pass1']['mess'] = 'Il faut le champ pass1'
            name_err['pass1']['err'] = 'invalid'
            return render(request, "signup.html", locals())
        if get_(request, 'pass2') == '':
            name_err['email']['mess'] = 'Good'
            name_err['email']['err'] = 'valid'
            value_email = get_(request, 'email')
            name_err['name_']['mess'] = 'Good'
            name_err['name_']['err'] = 'valid'
            value_name_ = get_(request, 'name_')
            name_err['pass1']['mess'] = 'Good'
            name_err['pass1']['err'] = 'valid'
            value_pass1 = get_(request, 'pass1')
            name_err['pass2']['mess'] = 'Il faut le champ pass2'
            name_err['pass2']['err'] = 'invalid'   
            return render(request, "signup.html", locals())
        if get_(request, 'pass1') != get_(request, 'pass2'):
            name_err['email']['mess'] = 'Good'
            name_err['email']['err'] = 'valid'
            value_email = get_(request, 'email')
            name_err['name_']['mess'] = 'Good'
            name_err['name_']['err'] = 'valid'
            value_name_ = get_(request, 'name_')
            name_err['pass1']['mess'] = 'Good'
            name_err['pass1']['err'] = 'valid'
            value_pass1 = get_(request, 'pass1')
            name_err['pass2']['mess'] = 'il faut un mot de pass identique'
            name_err['pass2']['err'] = 'invalid'
            return render(request, "signup.html", locals())


        pass1 = get_(request, 'pass1') #form.cleaned_data['pass_']
        name =  get_(request, 'name_') #form.cleaned_data['name']
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
    n=open('data.dt');user=n.read();n.close();del n
    open("data.dt", "w").close()
    Action(
        title='Log Out',
        from_app='home',
        user=user,
        body='deconextion'
        ).save()

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



