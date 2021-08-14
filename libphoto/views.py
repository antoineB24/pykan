import sys
sys.path.append('..')
from django.shortcuts import render
from django.http import HttpResponse
from home.models import Profil
from .models import Photo, PhotoForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models.fields.related_descriptors import ForeignKeyDeferredAttribute, ForwardManyToOneDescriptor
from django.db.models.query_utils import DeferredAttribute
import pandas as pd 


# Create your views here.


@login_required
def libphotos(request):
	user = request.user
	err = not user.is_authenticated
	dict_ = {'on' : True, 'off' : False}
	if not err:
		obj = user.profil
		form = PhotoForm(request.POST or None)
		
		lpp_global = Photo.objects.filter(est_parta=True)
		
		list_ = []
		
		lpp_cp = []
		for i in lpp_global:
			list_ = [n for n in i.parta.split('#') if n]
			if request.user.username in list_:
				list_.append(i)


		print(Photo.objects.all())
		lpp = list(Photo.objects.filter(author=request.user.username, est_parta=True)) + lpp_cp
		print(lpp)
		amie = [User.objects.get(username=i) for i in request.user.profil.amie.split('#') if bool(i)]
	if request.method == "POST":
		print(request.POST)
		p = Photo()
		p.author = request.user.username
		print(request.POST)

		p.image = request.POST.get('imgPr')
		p.comment = request.POST.get('commentPr')
		p.est_parta  = dict_[request.POST.get('is_par')]
		if p.est_parta:
			p.parta =  request.POST.get('parta_n') 
		p.save()
		print(p)


	return render(request, 'libphoto.html', locals())

@login_required
def photo_par(request):
	


	return render(request, 'photo_par.html', locals() )
def photo_priv(request):
	return HttpResponse('')
def to_pandas(db, field=None, list_field_object=None):
    list_= []
    field_copy = field
    list_field_object_copy = list_field_object
    if field == None or type(field) != list:
        field_copy = []
        for p in dir(db):
            
            if type(getattr(db, p)) in [DeferredAttribute,  ForeignKeyDeferredAttribute, ForwardManyToOneDescriptor]:
                field_copy.append(p)
    if type(list_field_object_copy) != list:
        list_field_object_copy = []
    for i in range(len(db.objects.all())):
        list_.append([])
        for n in field_copy:
            
            if type(getattr(db.objects.all()[i], str(n) )) in list_field_object_copy:
                list_[i].append(getattr(db.objects.all()[i], str(n) ))
            else: 
                list_[i].append(getattr(db.objects.all()[i], n) )

    return pd.DataFrame(list_, columns=field_copy)
print(to_pandas(Photo))
