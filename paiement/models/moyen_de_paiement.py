from django.db import models
from base.models.helpers.named_date_time_model import NamedDateTimeModel


# Create your models here.
class MethodeDePaiement(NamedDateTimeModel):

    class Meta:
        verbose_name = "Moyen de Paiement"
        verbose_name_plural = "Moyens de Paiement"
