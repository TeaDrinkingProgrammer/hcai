from django.http import HttpResponse
from django.template import loader
from hcai.__init__ import *
from django.shortcuts import render

def index(request):
    return render(request, "hcai/bad_app/result.html")