from django import forms

class BikeForm(forms.Form):
    name = forms.CharField(max_length=100)
    brand = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=150)
    email = forms.EmailField(required=False)
    password = forms.CharField(widget=forms.PasswordInput)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
