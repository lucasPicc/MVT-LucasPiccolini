from django.db import models

# Create your models here.
class Familiar(models.Model):
    edad = models.IntegerField()
    nombre = models.CharField(max_length=30)
    nacimiento = models.CharField(max_length=10)

