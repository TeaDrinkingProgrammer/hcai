from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label="Your name", required= True, max_length=100)
class GoodAppInputForm(forms.Form):
    carat_mg = forms.FloatField(label="Gewicht in mg", required= True)
    x = forms.FloatField(label="Lengte in mm", min_value=0, required= True)
    y = forms.FloatField(label="Breedte in mm", min_value=0, required= True)
    z = forms.FloatField(label="Diepte in mm", min_value=0, required= True)

class BadAppInputForm(forms.Form):
    carat_mg = forms.FloatField(label="Gewicht in mg", required= True)
    x = forms.FloatField(label="Lengte in mm", min_value=0, required= True)
    y = forms.FloatField(label="Breedte in mm", min_value=0, required= True)
    z = forms.FloatField(label="Diepte in mm", min_value=0, required= True)