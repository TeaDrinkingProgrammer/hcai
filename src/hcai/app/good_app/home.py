from hcai.__init__ import *
from django.shortcuts import render

from hcai.app.models import GoodAppFeedback

def index(request):
    def calc_avg():
        feedbacks = GoodAppFeedback.objects.all()
        avg = 0
        if len(feedbacks) > 0:
            avg = sum([feedback.rating for feedback in feedbacks]) / len(feedbacks)
        return round(avg, 2), len(feedbacks)
    avg_feedback, n_feedback = calc_avg()
    return render(request, "hcai/good_app/home.html", {"avg_feedback": avg_feedback, "n_feedback": n_feedback})