from django.contrib.auth import decorators
from django.db import models
from django.utils import timezone
# Create your models here.

class ApiJson(models.Model):
    author = models.CharField(max_length=50)
    id_json = models.CharField(max_length=75)
    date = models.DateTimeField(default=timezone.now)
    body = models.JSONField(default=dict)

    class Meta:
        verbose_name= 'Api Json'
        ordering = ['-date']
    
    def __str__(self):
        return self.id_json

