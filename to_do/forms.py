from django import forms
from django.forms import ModelForm

from .models import *

class To_doForm(forms.ModelForm):
    title=forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new Task....'}))

    class Meta:
        model=To_do
        fields='__all__'
