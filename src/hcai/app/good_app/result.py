import json
import string
from django.http import HttpRequest, HttpResponse
from django.template import loader
from hcai.__init__ import *
from django.shortcuts import redirect, render

from hcai.app.forms import FeedbackForm
from hcai.app.models import Feedback

def index(request: HttpRequest):
    if request.method == "POST":
        # Parse json from request body
        data = json.loads(request.body)
        # Get the rating from the request
        rating = data.get('rating', None)
        return HttpResponse(status=200)
    def calc_avg():
        feedbacks = Feedback.objects.all()
        avg = 0
        if len(feedbacks) > 0:
            avg = sum([feedback.rating for feedback in feedbacks]) / len(feedbacks)
        return avg
    
    rating = request.GET.get('rating', None)
    if rating is not None:
        # Get the rating from the request
        feedback = Feedback(rating=rating)
        feedback.save()
        # After the rating is given, redirect to the result page
        return render(request, "hcai/good_app/result.html", {"rating": rating})
    else:
        return render(request, "hcai/good_app/result.html",{"avg": calc_avg(), "rating": 0 })
    
