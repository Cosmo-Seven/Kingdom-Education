from django.db import models

class PriceEnum(models.TextChoices):
    EURO = "euro","Euro"
    MMK = "mmk","MMK"