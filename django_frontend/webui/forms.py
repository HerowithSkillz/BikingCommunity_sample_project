from django import forms

class BikeForm(forms.Form):
    name = forms.CharField(max_length=100)
    brand = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
