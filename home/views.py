import sys
sys.path.append('..')
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, Http404, HttpResponseForbidden
from django.conf import settings
from . import models
import string, random as rand
import re
from messenger.models import Messenger
from .models import Action, Notif
from django.utils import timezone
from forum.models import Forum
from blog.models import Blog, ForumBlog
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as log, logout
from django.contrib.auth.decorators import login_required
import pandas as pd
from django.db.models.query_utils import DeferredAttribute
from todolist.models import TodoList
from django.db.models.fields.related_descriptors import ForeignKeyDeferredAttribute, ForwardManyToOneDescriptor
from django.urls import reverse
from django.core.mail import send_mail

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
    pj
    n = open("data.dt", "r")
    
    user = request.user.is_authenticated
    
    n.close()
    obj = None
    if user:
        obj = request.user
        list_a = Action.objects.filter(user=obj.username).order_by('-date')
        notif = Messenger.objects.filter(destinataire=obj.username, new=True).count()
        notif_ = Messenger.objects.filter(destinataire=obj.username)
        a = Notif.objects.filter(from_app='messenger')
        obj_p = obj.profil
        for i in a:
            i.delete()
        for i in notif_:

            Notif(title=f"{i.sujet}", from_app='messenger', body=f'tu as recu un message de {i.author} à {i.date}', user=obj.username).save()
        list_m = Messenger.objects.all()
        notif_l = Notif.objects.filter(user=obj.username).order_by('-date')
        f = Forum.objects.order_by('date')[:5]
        b = Blog.objects.order_by('date')[:5]
        b_f = ForumBlog.objects.order_by('date')[:5]
        l_forum = Notif.objects.filter(from_app='forum', user=obj.username)
        l_blog = Notif.objects.filter(from_app='blog', user=obj.username)
        l_blog_forum = Notif.objects.filter(from_app='blog_forum', user=obj.username)
        for q in l_forum:
            q.delete()
        for q in l_blog:
            q.delete()

        for i in f:
            if i.user == user:
                continue
            Notif(title='Forum', from_app='forum', user=obj.username, body=f'{i.user} a posté un message').save()
        for i in b:
            if i.author == user:
                continue
            Notif(title=i.name, from_app='blog', user=obj.username, body=f'le Blog {i.name} a été créer par {i.author}').save()
        
        

    

    
    return render(request, "home.html", locals())

def login(request):
    

    if request.GET.get('next') == None:
        app = '/home'
    else:
        app = request.GET.get('next') 
    form  = models.Login(request.POST or None)
    if form.is_valid():
        obj_= authenticate(username=form.cleaned_data['name'], password=form.cleaned_data['pass_'])
        if obj_:
            log(request, obj_)
            return redirect('http://127.0.0.1:8000' + app)

    return render(request, "login.html", locals())
def signup(request):
    
    '''
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
        if User.objects.filter(username=get_(request, 'name_')).count() > 0:
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
        
        
        id_ = make_id(7)
        while any(in_fun(id_, models.Profil.objects.all())):
            id_ = make_id(7)
        

        u = User.objects.create_user(name, email, pass1)
        u.save()

        p = models.Profil( id_name=id_, user=u)
        p.save()
        
        log(request, u)

        return redirect('home')
    '''
            
    return render(request, "signup.html", locals())

def deconecte(request):
    
    Action(
        title='Log Out',
        from_app='home',
        user=request.user,
        body='deconextion'
        ).save()
    logout(request)

    return redirect('home')

def profil(request, idname):
    
    object_ = request.user
    err = not object_.is_authenticated

    obj = get_object_or_404(models.Profil, id_name=idname)
    #obj = models.Compte.objects.get(id_name=idname)
    
    co = False
    if not err and idname == object_.profil.id_name:
        co = True

    image_input = models.get_ChangeImgage()(request.POST or None, request.FILES)
    
    if request.method == "POST":
        if image_input.is_valid():
            obj.img_profil = image_input.cleaned_data['image']
            obj.save()
        

    
    string_set_pass_cmd = "/home/profil/%s/set_pass" % idname
    object_.profil.amie.split('#')
    if co:
        list_amie = [User.objects.get(username=i) for i in object_.profil.amie.split('#') if i]
    return render(request, 'profil.html', locals())

@login_required
def add_amie(request, idname):
    if not request.user.is_authenticated:
        return redirect('home')

    n = models.Profil.objects.filter(id_name=idname)
    
    user = request.user
    if n.count() == 0:
        raise Http404
    user.profil.amie = user.profil.amie + '#' + n[0].user.username
    user.profil.save()
    
    return redirect('home')

def set_pass(request, idname):
    
    obj = request.user
    user_co = obj.is_authenticated
    
    form = models.get_form_setPass(obj.username)(request.POST or None)
    if form.is_valid():
        obj.secrete = form.cleaned_data['new_pass2']
        obj.save()
    return render(request, 'set_pass.html', locals())


def to_pandas(db, field=None, list_field_object=None):
    list_= []
    field_copy = field
    list_field_object_copy = list_field_object
    if field == None or type(field) != list:
        field_copy = []
        for p in dir(db):
            
            if type(getattr(db, p)) in [DeferredAttribute,  ForeignKeyDeferredAttribute, ForwardManyToOneDescriptor]:
                field_copy.append(p)
    if type(list_field_object_copy) != list:
        list_field_object_copy = []
    for i in range(len(db.objects.all())):
        list_.append([])
        for n in field_copy:
            
            if type(getattr(db.objects.all()[i], str(n) )) in list_field_object_copy:
                list_[i].append(getattr(db.objects.all()[i], str(n) ))
            else: 
                list_[i].append(getattr(db.objects.all()[i], n) )

    return pd.DataFrame(list_, columns=field_copy)

def forgot(request):
    if  request.user.is_authenticated:
        return HttpResponseForbidden()
    if request.method == 'POST':

        object_  = get_object_or_404(User,email=request.POST.get('name'))
        send_mail('test',
            'ceci est un test',
            'tonio.barbier@gmail.com',
            [request.POST.get('name')])

    return HttpResponse('hello')





