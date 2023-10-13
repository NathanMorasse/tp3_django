from django.db import models

class Fermier(models.Model):
  prenom = models.CharField(max_length=50)
  nom = models.CharField(max_length=50)

  def __str__(self):
    return self.prenom + ' ' + self.nom
  
class Legume(models.Model):
  nom = models.CharField(max_length=50)
  famille = models.CharField(max_length=50)

  def __str__(self):
    return self.nom + ' ' + self.famille
