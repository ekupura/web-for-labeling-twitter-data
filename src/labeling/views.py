from django.shortcuts import render
from django.http import HttpResponse
from .models import Users
from django.template import loader

def index(request):
    user_list = Users.objects.order_by('id')[:10]
    template = loader.get_template('labeling/index.html')
    context = {
        'user_list': user_list,
    }
    return HttpResponse(template.render(context, request))
