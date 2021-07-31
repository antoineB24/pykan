from django.contrib import admin
from .models import Compte, Historique, Notif, Action

admin.site.register(Compte)
admin.site.register(Historique)
admin.site.register(Notif)
admin.site.register(Action)
