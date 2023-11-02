from django.http import HttpRequest
from hcai.app.forms import GoodAppInputForm
from hcai.__init__ import *
from django.shortcuts import render
from django.shortcuts import redirect

from hcai.app.models import GoodAppInput

def index(request: HttpRequest):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = GoodAppInputForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.cleaned_data["carat"] = form.cleaned_data["carat_mg"] * 0.005
            if form.cleaned_data["accept_terms"]:
                print("User accepted terms")
                databaseInput = GoodAppInput(x=form.cleaned_data["x"], y=form.cleaned_data["y"], z=form.cleaned_data["z"], carat=form.cleaned_data["carat"])
                databaseInput.save()
            else:
                print("User did not accept terms")
            # redirect to a new URL:
            print("Data" , form.cleaned_data)
            prediction = model.predict_good(form.cleaned_data["carat"], form.cleaned_data["x"], form.cleaned_data["y"], form.cleaned_data["z"])
            print("Predicted: ", prediction)
            request.session['prediction'] = round(prediction, 2)
            return redirect("/good_app/result")
    # if a GET (or any other method) we'll create a blank form
    else:
        form = GoodAppInputForm()

    return render(request, "hcai/good_app/questionaire.html", {"form": form})