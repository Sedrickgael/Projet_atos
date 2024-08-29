from django.db import models
from base.models.helpers.date_time_model import DateTimeModel
from base.models.helpers.named_date_time_model import NamedDateTimeModel


# Create your models here.
class Produit(NamedDateTimeModel):

    description = models.TextField()
    categorie_id = models.ForeignKey('boutique.Categorie', on_delete=models.CASCADE, related_name="categorie_produit_ids")
    vendeur_id = models.ForeignKey('boutique.Vendeur', on_delete=models.CASCADE, related_name="vendeur_produit_ids", null=True)
    tag_id = models.ManyToManyField('boutique.Tag', related_name="tag_produit_ids")
    prix = models.FloatField()

    class Meta:
        verbose_name = "Produit"
        verbose_name_plural = "Produits"
