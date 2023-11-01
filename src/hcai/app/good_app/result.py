from django.http import HttpResponse
from django.template import loader
from hcai.__init__ import *
from django.shortcuts import render

def index(request):
    print("formdata:", request.session.get('formdata'))
    return render(request, "hcai/good_app/result.html")