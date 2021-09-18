import sys
from django import forms as form
from django.core.checks import messages
sys.path.append('..')
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, QueryDict, Http404
from .models import GroupMsg, Messenger, MessengerForm
from home.models import  Action, Profil
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.forms.models import model_to_dict
from django.db.models.fields.related_descriptors import ManyToManyDescriptor

# Create your views here.

to_js = {True: 1, False: 0}

def to_dict_data(Class):
    dict_= dict()
    list_= list()

    for i in  Class:
        list_.append({'message_list' : [{**model_to_dict(n), 'date': str(n.date), 'started': to_js[n.started], 'draft': to_js[n.draft], 'new': to_js[n.new]} for n in i.messages.all()], 'author': i.author, 'destinataire': i.destinataire, 'subject': i.subject})
    return {'list': list_}
@login_required
def messenger(request):
    user = request.user
    nb_no_read = 0
    
    co = user.is_authenticated

    if co:
        obj1 = user.profil
    
        obj = GroupMsg.objects.filter(destinataire=user.username)
        print(obj)

        #print([model_to_dict(i) for i in obj])
        dict = to_dict_data(obj)
        print(dict)
        '''
        for i in obj:
            if i.new:
                nb_no_read += 1
        '''
    #return HttpResponse('hello')

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
    if request.method == 'POST':
        querydict = QueryDict(request.body.decode())
        if User.objects.filter(username=querydict.get('user')).exists():
            author = querydict.get('user')
        else:
            raise Http404()
        if querydict.get('object'):
            sujet= querydict.get('object')
        else:
            sujet='????'
        if querydict.get('contenue'):
            contenue=querydict.get('contenue')
        else:
            contenue=''
        groupmsg = GroupMsg(author=request.user, destinataire=author, subject=sujet)
        groupmsg.save()
        groupmsg.messages.create(author=author, sujet=sujet, body=contenue)



    return HttpResponse('')

def view(request, id):
    obj = get_object_or_404(Messenger, id=id)
    return render(request, 'view.html', locals())