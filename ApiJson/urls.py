from django.urls import path
from .views import *

urlpatterns = [
    path('', apijson, name='apijson'),
    path('api/new', new_api, name='new_api'),
    path('api/id/<path:id>', get_api, name='get_api'),
    path('api/list', list_api, name='list_api')
]