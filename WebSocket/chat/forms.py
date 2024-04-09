from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):

    username = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.TextInput)



