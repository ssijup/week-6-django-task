from django import forms
from .models import userdetails


class userform(forms.Modelform):

    class Meta:
        models = userdetails
