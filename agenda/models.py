from django.db import models

# Create your models here.

class Contato(models.Model):
    nome = models.CharField(max_length=20) 
    telefone = models.CharField(max_length=12)
    email = models.EmailField()
    usuario = models.CharField(max_length=20)
