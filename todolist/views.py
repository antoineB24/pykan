import json
import pprint
from json.encoder import JSONEncoder
import sys
sys.path.append('..')
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse,  JsonResponse, HttpResponseServerError

from .models import ActionTimeTable
from random import choice
from django.forms.models import model_to_dict
from home.models import Profil
from django.contrib.auth.decorators import login_required
import datetime



# Create your views here.


create_id = lambda id, len: ''.join([choice('azertyuiopqsdfghjklmwxcvbn1234567890') for i in range(len)]) + '.' + str(id)


@login_required
def todolist(request):
	idname = request.user.profil.id_name
	liste = []
	d = {}
	for i  in ActionTimeTable.objects.filter(author=request.user.username):
		liste.append({'id':i.id,'event_date':i.date_started.strftime("%a %b %d %Y"), 'event_title':i.action_name,'event_theme':i.theme})
	print(liste)
	user = request.user
	err = not user.is_authenticated
	return render(request, "todolist.html", locals())

def create(request):
	if request.method  == "POST":
	
		body = json.loads(request.body.decode('utf-8'))
		title = body.get('title')
		date = body.get('date')
		theme = body.get('theme')
		
		#Mon Sep 06 2021
		d=datetime.datetime.strptime(date, "%a %b %d %Y")
		ActionTimeTable(date_started=d, action_name=title, theme=theme,author=request.user.username).save()
		return JsonResponse({})
	
	return JsonResponse({})
	


def liste(request):
	liste = []
	d = {}
	for i  in ActionTimeTable.objects.filter(author=request.user.username):
		liste.append({'id':i.id,'event_date':i.date_started.strftime("%a %b %d %Y"), 'event_title':i.action_name,'event_theme':i.theme})
	
	
	return JsonResponse({'list': liste})

def delete(request):
	if request.method == "POST":
		body = json.loads(request.body.decode('utf-8'))
		id = body.get('id')
		o = ActionTimeTable.objects.get(pk=id)
		o.delete()

