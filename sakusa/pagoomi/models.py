from django.db import models
from django.urls import reverse
import uuid

# Create your models here.

class Curiosidad(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)

    class Meta:
      ordering = ['name']

    def __str__(self):
        return self.name
