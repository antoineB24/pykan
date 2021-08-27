"""pyforum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from os import name
from django.contrib import admin
from django.urls import path, include
from .views import home, login, signup, deconecte, profil, add_amie,forgot
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('login', login, name='login'),
    path('signup', signup, name='signup'),
    path('deconecte', deconecte, name='deconecte'),
    path('profil/<path:idname>/', profil, name='profil'),
    path('add_amie/<path:idname>/', add_amie, name='add_amie'),
    path('forgot_pass/', forgot ,name='forgot')
    #path('profil/<str:idname>/set_pass', set_pass, name='set_pass')
]
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
