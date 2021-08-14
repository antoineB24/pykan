from django.contrib import admin
from .models import  Historique, Notif, Action, Profil


admin.site.register(Historique)
admin.site.register(Notif)
admin.site.register(Action)
admin.site.register(Profil)
