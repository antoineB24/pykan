
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import *
import random, string
import json


# Create your views here.


make_id = lambda l: ''.join([random.choice(string.ascii_letters + '1234567890') for i in range(l)])

@login_required
def apijson(request):
    return render(request, 'apijson.html', locals())


def new_api(request):

    if request.method == "POST":
        dict_ = request.POST['json']
        dict_ = json.dumps(dict_)
        if type(dict_) == dict:
            pass
        else:
            try:
                dict_ = json.loads(dict_)
            except Exception as e:
                print(e)
                return JsonResponse({'msg' : 'Error format json invalid: ' }, status=500)
            else:
                dict_ = json.loads(dict_)

        id_ = make_id(30)
        
        ApiJson(author=request.POST['author'], id_json=id_, body=dict_).save()


        return JsonResponse({"id": id_ })
    return JsonResponse({})


def get_api(request, id):
    obj = get_object_or_404(ApiJson, id_json=id)
    return JsonResponse(obj.body)
def list_api(request):
    print(ApiJson.objects.all())
    list_ = [{'id' : a.id, 'id_json' : a.id_json} for a in ApiJson.objects.filter(author=request.user.username)]
    return JsonResponse({'list': list_})