from django.contrib import admin
from .models import Messenger, GroupMsg

# Register your models here.


admin.site.register(Messenger)
admin.site.register(GroupMsg)