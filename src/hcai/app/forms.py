from django import forms

from hcai.app.models import Feedback

class NameForm(forms.Form):
    your_name = forms.CharField(label="Your name", required= True, max_length=100)
class GoodAppInputForm(forms.Form):
    carat_mg = forms.FloatField(label="Gewicht in mg", min_value=40, required= True)
    x = forms.FloatField(label="Lengte in mm", min_value=2, required= True)
    y = forms.FloatField(label="Breedte in mm", min_value=2, required= True)
    z = forms.FloatField(label="Diepte in mm", min_value=2, required= True)

class BadAppInputForm(forms.Form):
    carat_mg = forms.FloatField(label="Gewicht in mg", min_value=40, required= True)
    x = forms.FloatField(label="Lengte in mm", min_value=2, required= True)
    y = forms.FloatField(label="Breedte in mm", min_value=2, required= True)
    z = forms.FloatField(label="Diepte in mm", min_value=2, required= True)

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        exclude = []
