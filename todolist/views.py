import sys
sys.path.append('..')
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse,  JsonResponse, HttpResponseServerError

from .models import Time, TimeBody, TodoList
from random import choice
from django.forms.models import model_to_dict
from home.models import Profil
from django.contrib.auth.decorators import login_required


# Create your views here.


create_id = lambda id, len: ''.join([choice('azertyuiopqsdfghjklmwxcvbn1234567890') for i in range(len)]) + '.' + str(id)


@login_required
def todolist(request):
	user = request.user
	err = not user.is_authenticated

	if not err:
		obj = user.profil
		idname = obj.id_name
		time_list = Time.objects.filter(user=user.username)
		time_body_list = TimeBody.objects.filter(user=user.username)
		todolist_ = TodoList.objects.filter(user=user.username)


	if request.method == 'POST':
		if request.POST.get('name_') is  not None:
			if request.POST.get('name_') == '':
				return render(request, "todolist.html", locals())
			if request.POST.get('date') == '':
			  	return render(request, "todolist.html", locals())
			date = request.POST.get('date')
			name = request.POST.get('name_')
			Time(user=user.username, date_started=date, name=name).save()
		if not (request.POST.get('heure') is  None):
			last = TimeBody.objects.filter(user=user.username, name_time=request.GET.get('time_n')).last()

			if request.POST.get('heure') == '':
				return render(request, "todolist.html", locals())
			if not request.POST['heure'].isdigit():
				return render(request, "todolist.html", locals())
			if request.POST['minute'] == '':
				return render(request, "todolist.html", locals())
			if not request.POST['minute'].isdigit():
				return render(request, "todolist.html", locals())

			if int(request.POST['heure']) > 24 or int(request.POST['heure']) < 0:
				 return render(request, "todolist.html", locals())
			if int(request.POST['minute']) > 24 or int(request.POST['minute']) < 0:
				 return render(request, "todolist.html", locals())
			if last:
				if int(request.POST['heure']) < int(last.hours) and int(request.POST['minute']) < int(last.minute) :
					return render(request, "todolist.html", locals())




			if request.POST['body'] ==  '':
				return render(request, "todolist.html", locals())
			heure = int(request.POST['heure'])
			minute = int(request.POST['minute'])
			f = lambda o, n : [getattr(i, n) for i in o ]
			body = request.POST['body']
			if request.GET.get('time_n') not in f(Time.objects.all(), 'name'):
				return render(request, "todolist.html", locals())
			TimeBody(
			 user=user.username,
			 name=create_id(request.GET.get('time_n'), 5),
			 hours=heure, 
			 minute=minute,
			 body=body,
			 name_time=request.GET.get('time_n')
			 ).save()
		if not (request.POST.get('todo_item') is None):
			for i in time_body_list:
				if i.name == request.GET.get('name_time'):
					
					TodoList(user=user.username, action=request.POST.get('todo_item'), time_body_name=request.GET.get('name_time')).save()

			

	return render(request, "todolist.html", locals())

@login_required
def create(request, name):
	user = request.user
	obj = get_object_or_404(TimeBody, name=name)
	n = TimeBody.objects.get(name=name, user=user.username)
	n.is_todolist = True
	n.save()
	return redirect('todolist')

@login_required
def set_time_1(request):
	if request.method == 'POST':
		n = TodoList.objects.get(id=request.POST.get('id') )
		n.checked = not n.checked
		n.save()
	return JsonResponse({"id": request.POST.get('id') } )

@login_required
def set_time_2(request):
	if request.method == "POST":
		n = request.POST.get("id_delete")
		try:
			obj = TodoList.objects.get(id=n)
		except:
			return HttpResponseServerError("ERROR")
		else:
			obj = TodoList.objects.get(id=n)
		obj.delete()

	return JsonResponse({'id' : n})