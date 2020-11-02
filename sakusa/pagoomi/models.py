from django.db import models
from django.urls import reverse
import uuid

# Create your models here.

class Curiosidad(models.Model):
    name = models.CharField(max_length=200, help_text="Introduzca un breve título de la curiosidad")
    description = models.TextField(max_length=1000, help_text="Introduzca una breve descripción de la curiosidad")

    def __str__(self):
        return self.name
