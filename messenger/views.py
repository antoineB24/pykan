import sys
from django import forms as form
from django.core.checks import messages
from django.http.response import JsonResponse

sys.path.append('..')
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, QueryDict, Http404
from .models import GroupMsg, Messenger, MessengerForm
from home.models import Action, Profil
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.forms.models import model_to_dict
from django.views import View
import json, pprint

# Create your views here.

to_js = {True: 1, False: 0}


def to_dict_data(_class):
    dict_ = dict()
    list_ = list()

    for i in _class:
        list_.append({'message_list': [
            {**model_to_dict(n), 'date': str(n.date), 'started': to_js[n.started], 'draft': to_js[n.draft],
             'new': to_js[n.new], 'img_src': User.objects.get(username=n.author).profil.img_profil.url} for n in
            i.messages.all()], 'author': i.author, 'destinataire': i.destinataire, 'subject': i.subject})
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

        # print([model_to_dict(i) for i in obj])
        dict = to_dict_data(obj)
        print(dict)
        '''
        for i in obj:
            if i.new:
                nb_no_read += 1
        '''
    # return HttpResponse('hello')

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
            sujet = querydict.get('object')
        else:
            sujet = '????'
        if querydict.get('contenue'):
            contenue = querydict.get('contenue')
        else:
            contenue = ''
        groupmsg = GroupMsg(author=request.user, destinataire=author, subject=sujet)
        groupmsg.save()
        groupmsg.messages.create(author=request.user.username, sujet=sujet, body=contenue)

    return HttpResponse('')

class Reply(View):
    http_method_names = ["get", "post"]

    def post(self, request, *args, **kwargs):
        data = request.body.decode()
        query = QueryDict(data)
        actual_mess = json.loads(query.get('actual_mess'))
        l = Messenger.objects.get(id=int(actual_mess['message_list'][0]['id'])).groupmsg_set.all()
        l[0].messages.create(body=query.get("reply"), author=request.user.username,
                             destinataire=actual_mess['message_list'][0]['destinataire'],
                             sujet=actual_mess['subject'])
        return JsonResponse({"res": "OK"})

    def get(self, request, *args, **kwargs):
        return JsonResponse({"res": "Forbiden"}, status=403)

