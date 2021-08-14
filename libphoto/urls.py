from django.urls import path
from .views import libphotos, photo_par, photo_priv

urlpatterns = [
	path('', libphotos, name='libphotos'),
	path('photo_par', photo_par, name='photo_par'),
	path('photo_priv', photo_priv , name='photo_priv')
]