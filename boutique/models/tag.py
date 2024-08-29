from django.db import models
from base.models.helpers.date_time_model import DateTimeModel
from base.models.helpers.named_date_time_model import NamedDateTimeModel


# Create your models here.
class Tag(NamedDateTimeModel):

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"