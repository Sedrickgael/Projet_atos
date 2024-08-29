from django.db import models
from base.models.helpers.date_time_model import DateTimeModel
from base.models.helpers.named_date_time_model import NamedDateTimeModel


# Create your models here.
class Avis(DateTimeModel):

    client_id = models.ForeignKey('customer.Client', on_delete=models.CASCADE, related_name="avis_client_ids")
    produit_id = models.ForeignKey('boutique.Produit', on_delete=models.CASCADE, related_name="avis_produit_ids")
    note =  models.FloatField(help_text="Donnez une note entre 0 et 5"
                              )
    class Meta:
        verbose_name = "Avis"
        verbose_name_plural = "Avis"