import json
from django.http import HttpRequest, HttpResponse
from hcai.__init__ import *
from django.shortcuts import render

from hcai.app.models import GoodAppFeedback

def index(request: HttpRequest):
    def calc_avg():
        feedbacks = GoodAppFeedback.objects.all()
        avg = 0
        if len(feedbacks) > 0:
            avg = sum([feedback.rating for feedback in feedbacks]) / len(feedbacks)
        return round(avg, 1), len(feedbacks)
    
    if request.method == "POST":
        # Parse json from request body
        data = json.loads(request.body)
        # Get the rating from the request
        rating = data.get('rating', None)
        feedback = GoodAppFeedback(rating=rating)
        feedback.save()
        return HttpResponse(status=200)
    form = request.session.get('form', '')
    model_type = request.session.get('model_type', '')
    plot, texts = model.shap(model_type, form["carat"], form["x"], form["y"], form["z"])
    rating = request.GET.get('rating', None)
    avg, n_votes = calc_avg()
    if rating is not None:
        # Get the rating from the request
        # After the rating is given, redirect to the result page
        return render(request, "hcai/good_app/result.html", {"avg": avg, "n_votes": n_votes, "rating": rating, "prediction": request.session.get('prediction', ''), "plot": plot, "texts": texts})
    else:
        return render(request, "hcai/good_app/result.html",{"avg": avg, "n_votes": n_votes, "rating": 0, "prediction": request.session.get('prediction', ''), "plot": plot, "texts": texts})
    
