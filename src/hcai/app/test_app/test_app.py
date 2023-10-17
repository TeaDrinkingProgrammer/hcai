from django.http import HttpResponse
from django.template import loader
from hcai.__init__ import *
from django.shortcuts import render

def index(request):
    
    modeltest = model.test()
    header = modeltest[1]
    data = modeltest[0]
    image = modeltest[2].to_html()
    context = {
        "header": header,
        "data": data,
        "tests": image,
    }
    return render(request, "hcai/test.html", context)