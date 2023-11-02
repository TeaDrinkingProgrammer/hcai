import json
from django.http import HttpRequest, HttpResponse
from hcai.__init__ import *
from django.shortcuts import redirect, render

from hcai.app.models import Feedback

def index(request: HttpRequest):
    def calc_avg():
        feedbacks = Feedback.objects.all()
        avg = 0
        if len(feedbacks) > 0:
            avg = sum([feedback.rating for feedback in feedbacks]) / len(feedbacks)
        return round(avg, 2), len(feedbacks)
    
    if request.method == "POST":
        # Parse json from request body
        data = json.loads(request.body)
        # Get the rating from the request
        rating = data.get('rating', None)
        feedback = Feedback(rating=rating)
        feedback.save()
        return HttpResponse(status=200)
    
    rating = request.GET.get('rating', None)
    avg, n_votes = calc_avg()
    if rating is not None:
        # Get the rating from the request
        # After the rating is given, redirect to the result page
        return render(request, "hcai/bad_app/result.html", {"avg": avg, "n_votes": n_votes, "rating": rating, "prediction": request.session.get('prediction', '')})
    else:
        return render(request, "hcai/bad_app/result.html",{"avg": avg, "n_votes": n_votes, "rating": 0, "prediction": request.session.get('prediction', '') })
    
