from django.db import models
from base.models.helpers.date_time_model import DateTimeModel


# Create your models here.
class Panier(DateTimeModel):

    client_id = models.ForeignKey('customer.Client', on_delete=models.SET_NULL, null=True, related_name='panier_clients_ids')
    produit_ids = models.ManyToManyField('boutique.Produit', related_name="panier_produit_ids")

    class Meta:
        verbose_name = "Panier"
        verbose_name_plural = "Paniers"

    def __str__(self):
        return str(self.id)