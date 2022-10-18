from django.db import models

class Types(models.Model):
    type = models.CharField(max_length=1, unique=True)
    description = models.TextField()
    natureza = models.CharField(max_length=10)
    sinal = models.CharField(max_length=1)
