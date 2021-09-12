
from django.db import models
from django.utils import timezone

# Create your models here.

class ActionTimeTable(models.Model):
	THEME = (('blue', "Blue Theme"),
		('red', "Red Theme"),
		("yellow", "Yellow Theme"),
		("green" , "Greene Theme "),
		("purple", "Purple Theme"))
	

	action_name = models.CharField(max_length=100)
	date_created = models.DateTimeField(default=timezone.now, verbose_name="date: ")
	date_started = models.DateTimeField()
	theme = models.CharField(max_length=50, choices=THEME, default='blue')
	author= models.CharField(max_length=50, default='')


	class Meta:
		verbose_name="Action Time Table"
		
	
	def __str__(self):
		return self.action_name
	




