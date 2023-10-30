from hcai.app.forms import GoodAppInputForm
from django.http import HttpResponseRedirect
from hcai.__init__ import *
from django.shortcuts import render

def index(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = GoodAppInputForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.cleaned_data["carat"] = form.cleaned_data["carat_mg"] * 0.005

            # redirect to a new URL:
            print("Data" , form.cleaned_data)
            prediction = model.predict(form.cleaned_data["carat"], form.cleaned_data["x"], form.cleaned_data["y"], form.cleaned_data["z"])
            print("Predicted: ", prediction)
            return HttpResponseRedirect("/good_app/explanation")
    # if a GET (or any other method) we'll create a blank form
    else:
        form = GoodAppInputForm()

    return render(request, "hcai/good_app/questionaire.html", {"form": form})