from django.contrib import admin
from .models import TodoList, TimeBody, Time

# Register your models here.

admin.site.register(TodoList)
admin.site.register(TimeBody)
admin.site.register(Time)

