from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Users, Search
import pprint
import random

def guhehe(request):
    return HttpResponse('ぐへへ')

def index(request):
    user_query = random.choice(Users.objects.filter(nit=-1))
    search_query = Search.objects.filter(user_id=user_query.id)[:5]
    template = loader.get_template('labeling/index.html')
    context = {
        'user': user_query,
        'search': search_query,
    }
    return HttpResponse(template.render(context, request))

def vote(request, user_id):
    choice = request.POST['choice']
    user = Users.objects.filter(id=user_id)[0]
    user.nit = (1 if choice == "OK" else (2 if choice == "OB" else 0))
    user.save()
    return HttpResponseRedirect(reverse('index'))
