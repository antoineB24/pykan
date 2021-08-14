from django.db import models
from django.utils import timezone
from django import forms


# Create your models here.

class Photo(models.Model):
	author = models.CharField(max_length=50)
	comment = models.CharField(max_length=50)
	image = models.ImageField(upload_to='libphoto/')
	title = models.CharField(max_length=50, default='')
	est_parta = models.BooleanField(default=False)
	parta = models.CharField(max_length=300, blank=False, default='')
	date = models.DateTimeField(default=timezone.now, verbose_name='date')
	class Meta:
		verbose_name = 'Photo'
		ordering = ['date']
	def __str__(self):
		return self.author

class PhotoForm(forms.Form):
	image = forms.ImageField(required=True)
	comment = forms.CharField(required=False, widget=forms.Textarea, label='Commentaire: ')
	title = forms.CharField(required=True, label='titre: ')






