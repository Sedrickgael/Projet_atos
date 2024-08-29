from django.db import models
from base.models.helpers.date_time_model import DateTimeModel


# Create your models here.
class Commande(DateTimeModel):

    client_id = models.ForeignKey('customer.Client', on_delete=models.SET_NULL, null=True, related_name='commande_clients_ids')
    panier_id = models.ForeignKey('customer.Panier', on_delete=models.CASCADE, null=True, related_name='commande_panier_ids')
    date_commande = models.DateTimeField()
    active_paiement = models.BooleanField(default=False)
    active_livraison = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Commande"
        verbose_name_plural = "Commandes"

    def __str__(self):
        return str(self.id)