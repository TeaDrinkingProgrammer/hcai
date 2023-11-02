from django.http import HttpResponseRedirect
from hcai.__init__ import *
from django.shortcuts import render
from django.shortcuts import redirect
from hcai.app.forms import BadAppInputForm

from hcai.app.models import BadAppInput

def index(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = BadAppInputForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.cleaned_data["carat"] = round(form.cleaned_data["carat_mg"] * 0.005, 4)

            databaseInput = BadAppInput(x=form.cleaned_data["x"], y=form.cleaned_data["y"], z=form.cleaned_data["z"], carat=form.cleaned_data["carat"])
            databaseInput.save()
            print("Data stored")

            # redirect to a new URL:
            print("Data" , form.cleaned_data)
            prediction = model.predict_bad(form.cleaned_data["carat"], form.cleaned_data["x"], form.cleaned_data["y"], form.cleaned_data["z"], form.cleaned_data["quick_sell"])
            print("Predicted: ", prediction)
            request.session['prediction'] = round(prediction, 2)
            request.session['quick_sell'] = form.cleaned_data["quick_sell"]
            return redirect("/bad_app/result")
    # if a GET (or any other method) we'll create a blank form
    else:
        form = BadAppInputForm()

    return render(request, "hcai/bad_app/questionaire.html", {"form": form})