from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template("hcai/good_app.html")
    context = {
        "test_bool": True,
    }
    return HttpResponse(template.render(context, request))