from django.db import models
from base.models.helpers.date_time_model import DateTimeModel


# Create your models here.
class Livraison(DateTimeModel):

    commande_id = models.ForeignKey('customer.Commande', on_delete=models.CASCADE, null=True, related_name='livraison_commande_id')
    date_livraison = models.DateTimeField()
    active = models.BooleanField()
    
    class Meta:
        verbose_name = "Livraison"
        verbose_name_plural = "Livraisons"

    def __str__(self):
        return str(self.id)