from django.db import models
# Create your models here.


class Personne(models.Model):
    nom = models.CharField(max_length=200, null=False)
    prenom = models.CharField(max_length=200, null=False)

    def __str__(self) -> str:
        return str(self.prenom) + ' ' + str(self.nom)
