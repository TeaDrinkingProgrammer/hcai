from django.db import models
class GoodAppFeedback(models.Model):
    rating = models.PositiveSmallIntegerField()

class BadAppFeedback(models.Model):
    rating = models.PositiveSmallIntegerField()

class GoodAppInput(models.Model):
    carat = models.FloatField()
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField()

class BadAppInput(models.Model):
    carat = models.FloatField()
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField()