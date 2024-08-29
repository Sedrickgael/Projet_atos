from django.db import models
from base.models.helpers.date_time_model import DateTimeModel


# Create your models here.
class Paiement(DateTimeModel):

    commande_id = models.ForeignKey('customer.Commande', on_delete=models.CASCADE, null=True, related_name='paiement_commande_id')
    moyen_de_paiement_id = models.ForeignKey('paiement.MethodeDePaiement', on_delete=models.SET_NULL, null=True, related_name="paiement_ids")
    date_paiement = models.DateTimeField()
    status_paiement = models.BooleanField()

    
    class Meta:
        verbose_name = "Paiement"
        verbose_name_plural = "Paiements"

    def __str__(self):
        return str(self.id)