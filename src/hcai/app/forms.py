from django import forms
from django.utils.html import format_html

from hcai.app.models import Feedback

class NameForm(forms.Form):
    your_name = forms.CharField(label="Your name", required= True, max_length=100)
class GoodAppInputForm(forms.Form):
    carat_mg = forms.FloatField(label="Gewicht in mg", min_value=40, required= True)
    x = forms.FloatField(label="Lengte in mm", min_value=2, required= True)
    y = forms.FloatField(label="Breedte in mm", min_value=2, required= True)
    z = forms.FloatField(label="Diepte in mm", min_value=2, required= True)
    # Style is the same as h-8 w-8
    accept_terms = forms.BooleanField(label = format_html("Click here to accept <a href='/good_app/privacy' a>the privacy policy</a>"),required= False, widget=forms.CheckboxInput(attrs={'style': 'width:2rem; height: 2rem'}))
from django.utils.html import format_html

class BadAppInputForm(forms.Form):
    carat_mg = forms.FloatField(label="Gewicht in mg", min_value=40, required= True)
    x = forms.FloatField(label="Lengte in mm", min_value=2, required= True)
    y = forms.FloatField(label="Breedte in mm", min_value=2, required= True)
    z = forms.FloatField(label="Diepte in mm", min_value=2, required= True)

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        exclude = []
