from django.db import models
from base.models.helpers.named_date_time_model import NamedDateTimeModel


# Create your models here.
class Client(NamedDateTimeModel):

    name = models.CharField(max_length=180, verbose_name="Nom")
    prenoms = models.CharField(max_length=180, verbose_name="Prénoms")
    adresse = models.TextField()
    pays = models.CharField(max_length=50)  # il est possible d'avoir une entité pays ou d'utiliser des packages
    ville = models.CharField(max_length=50)  # il est possible d'avoir une entité ville ou d'utiliser des packages
    active = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"