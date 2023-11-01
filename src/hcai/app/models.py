from django.db import models
class Feedback(models.Model):
    rating = models.PositiveSmallIntegerField()