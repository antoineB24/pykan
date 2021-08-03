from django.db import models
from django.utils import timezone

# Create your models here.

class TodoList(models.Model):
	user = models.CharField(max_length=50)
	name = models.CharField(max_length=50, blank=False)
	action = models.CharField(max_length=50, blank=False)
	time_body_name = models.CharField(max_length=30)
	barre = models.BooleanField(default=False)
	checked = models.BooleanField(default=False)



class TimeBody(models.Model):
	user = models.CharField(max_length=50)
	name = models.CharField(max_length=50, blank=False)
	hours = models.CharField(max_length=20, blank=False)
	minute = models.CharField(max_length=20, blank=False)
	body = models.CharField(max_length=200, blank=False)
	name_time = models.CharField(max_length=50)
	is_todolist = models.BooleanField(default=False)
	

class Time(models.Model):
	user = models.CharField(max_length=50)
	name = models.CharField(max_length=50)
	date_created = models.DateTimeField(default=timezone.now, verbose_name='date')
	date_started = models.CharField(max_length=30)
	




