from django import forms
from django.utils.html import format_html

from hcai.app.models import BadAppFeedback, GoodAppFeedback

class NameForm(forms.Form):
    your_name = forms.CharField(label="Your name", required= True, max_length=100)
class GoodAppInputForm(forms.Form):
    carat_mg = forms.FloatField(label="Gewicht in mg", min_value=40, required= True)
    x = forms.FloatField(label="Lengte in mm", min_value=2, required= True)
    y = forms.FloatField(label="Breedte in mm", min_value=2, required= True)
    z = forms.FloatField(label="Diepte in mm", min_value=2, required= True)
    # Style is the same as h-8 w-8
    accept_terms = forms.BooleanField(label = format_html("Ik accepteer dat mijn data anoniem verwerkt wordt volgens de <a href='/good_app/privacy' a>privacyvoorwaarden</a>. Dit is niet verplicht."),required= False, widget=forms.CheckboxInput(attrs={'style': 'width:2rem; height: 2rem'}))

class BadAppInputForm(forms.Form):
    carat_mg = forms.FloatField(label="Gewicht in mg", min_value=40, required= True)
    x = forms.FloatField(label="Lengte in mm", min_value=2, required= True)
    y = forms.FloatField(label="Breedte in mm", min_value=2, required= True)
    z = forms.FloatField(label="Diepte in mm", min_value=2, required= True)
    quick_sell = forms.BooleanField(label = "Verkoop je diamand snel aan onze partner",required= False, widget=forms.CheckboxInput(attrs={'style': 'width:2rem; height: 2rem'}))
    # Style is the same as h-8 w-8
    accept_terms = forms.BooleanField(label = format_html("Klik hier om de <a href='/bad_app/privacy' a>privacyvoorwaarden</a> te accepteren."),required= True, widget=forms.CheckboxInput(attrs={'style': 'width:2rem; height: 2rem'}))

class GoodAppFeedbackForm(forms.ModelForm):
    class Meta:
        model = GoodAppFeedback
        exclude = []

class BadAppFeedbackForm(forms.ModelForm):
    class Meta:
        model = BadAppFeedback
        exclude = []
