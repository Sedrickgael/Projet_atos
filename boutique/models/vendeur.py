from django.db import models
from base.models.helpers.date_time_model import DateTimeModel
from base.models.helpers.named_date_time_model import NamedDateTimeModel


# Create your models here.
class Vendeur(DateTimeModel):

    nom_boutique = models.CharField(max_length=180, verbose_name="Nom de la boutique")
    name = models.CharField(max_length=180, verbose_name="Nom")
    prenoms = models.CharField(max_length=180, verbose_name="Prénoms")
    adresse = models.TextField()
    pays = models.TextField()  # il est possible d'avoir une entité pays ou d'utiliser des packages
    ville = models.TextField()  # il est possible d'avoir une entité ville ou d'utiliser des packages
    active = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Vendeur"
        verbose_name_plural = "Vendeurs"
    
    def __str__(self):
        return self.name