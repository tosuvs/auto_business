from django.db import models
from core.filters_models_field.decimal_range_field import DecimalRangeField
from django_countries.fields import CountryField


class Information(models.Model):
    name = models.CharField(max_length=50)
    balance = DecimalRangeField(max_digits=20, decimal_places=2, min_value=0.00, default=0.00)
    country = CountryField(multiple=True)
    email = models.EmailField(max_length=254)

    class Meta:
        abstract = True