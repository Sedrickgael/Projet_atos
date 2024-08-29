from django.db import models
from base.models.helpers.date_time_model import DateTimeModel
from base.models.helpers.named_date_time_model import NamedDateTimeModel


# Create your models here.
class Categorie(NamedDateTimeModel):

    description = models.TextField()
    
    class Meta:
        verbose_name = "Catégorie"
        verbose_name_plural = "Catégories"