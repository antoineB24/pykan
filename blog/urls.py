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
from .views import blog, create_blog, write_mess, go_blog
from django.views.generic import RedirectView

urlpatterns = [
    path('', blog, name='blog'),
    path('main', RedirectView.as_view(pattern_name='blog')),
    path('create_blog', create_blog, name='create_blog'),
    path('write_mess', write_mess, name='write_mess'),
    path('id/<str:idblog>', go_blog,name='')
]
