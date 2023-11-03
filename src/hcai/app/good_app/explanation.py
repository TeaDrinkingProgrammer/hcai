from hcai.__init__ import *
from django.shortcuts import render

def index(request):
    return render(request, "hcai/good_app/explanation.html")