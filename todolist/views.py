import sys
sys.path.append('..')
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from home.models import Compte
from .models import Time, TimeBody, TodoList
from random import choice

# Create your views here.


create_id = lambda id, len: ''.join([choice('azertyuiopqsdfghjklmwxcvbn1234567890') for i in range(len)]) + '.' + str(id)



def todolist(request):
	n=open('data.dt');user=n.read();n.close()
	err = not bool(user)

	if not err:
		obj = Compte.objects.get(name=user)
		idname = obj.id_name
		time_list = Time.objects.filter(user=user)
		time_body_list = TimeBody.objects.filter(user=user)
		todolist_ = TodoList.objects.filter(user=user)


	if request.method == 'POST':
		if request.POST.get('name_') is  not None:
			if request.POST.get('name_') == '':
				return render(request, "todolist.html", locals())
			if request.POST['date'] == '':
			  	return render(request, "todolist.html", locals())
			date = request.POST['date']
			name = request.POST['name']
			Time(user=user, date_started=date, name=name).save()
		if not (request.POST.get('heure') is  None):
			last = TimeBody.objects.filter(user=user, name_time=request.GET.get('time_n')).last()

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
				if int(request.POST['heure']) < last.hours and int(request.POST['minute']) < last.minute :
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
			 user=user,
			 name=create_id(request.GET.get('time_n'), 5),
			 hours=heure, 
			 minute=minute,
			 body=body,
			 name_time=request.GET.get('time_n')
			 ).save()
		if not (request.POST.get('todo_item') is None):
			for i in time_body_list:
				if i.name == request.GET.get('name_time'):
					print('1')
					TodoList(user=user, action=request.POST.get('todo_item'), time_body_name=request.GET.get('name_time')).save()

			

	return render(request, "todolist.html", locals())


def create(request, name):
	n=open('data.dt');user=n.read();n.close()
	obj = get_object_or_404(TimeBody, name=name)
	TodoList(user=user, name=name + '//todo', time_body_name=name).save()
	n = TimeBody.objects.get(name=name, user=user)
	n.is_todolist = True
	n.save()
	return redirect('home')