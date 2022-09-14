from cgitb import text
import email
from socket import fromshare
from unicodedata import name
from django import forms

class forName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)