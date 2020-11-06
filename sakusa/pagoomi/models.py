from django.db import models
from django.urls import reverse
import uuid

# Create your models here.

class Curiosidad(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)

    class Meta:
      ordering = ['name']

    def __str__(self):
        return self.name

class Formulario(models.Model):
    identificador = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    email  = models.EmailField()
    comentario = models.CharField(max_length=2000)
