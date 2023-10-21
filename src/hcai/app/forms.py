from django import forms
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Field, Fieldset, Submit

input_widget = forms.NumberInput(attrs={'class': 'text-black'})

class NameForm(forms.Form):
    your_name = forms.CharField(label="Your name", required= True, max_length=100)
class GoodAppInputForm(forms.Form):
    carat_mg = forms.FloatField(label="Gewicht in mg", required= True, widget= input_widget)
    x = forms.FloatField(label="Lengte in mm", min_value=0, required= True, widget= input_widget)
    y = forms.FloatField(label="Breedte in mm", min_value=0, required= True, widget= input_widget)
    z = forms.FloatField(label="Diepte in mm", min_value=0, required= True, widget= input_widget)