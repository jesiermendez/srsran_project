from django import forms
from django.contrib.auth.forms import AuthenticationForm

# Create your forms here.
class CustomUserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus': True}))

    