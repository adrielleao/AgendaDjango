from django import forms
# from models import Contato
# from django.forms import ModelForm

class ContatoForm(forms.Form):
    nome = forms.CharField(max_length=20) 
    telefone = forms.CharField(max_length=12)
    email = forms.EmailField()
    usuario = forms.CharField(max_length=20)