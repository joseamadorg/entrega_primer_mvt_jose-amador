from django.db import models

# Create your models here.

class Familiar(models.Model):
  nombre = models.CharField(max_length=250)
  documento = models.CharField(max_length=250)
  nacimiento = models.CharField(max_length=250)

  def __str__(self):
      return self.nombre

  def __num__(self):
      return self.documento

  def __date__(self):
      return self.nacimiento
