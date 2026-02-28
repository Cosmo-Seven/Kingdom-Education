from django.db import models
from django.utils.text import slugify
from models.base_models import BaseModel


class PaymentMethodModel(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    number = models.CharField(max_length=100)
    featured_image = models.ImageField(
        upload_to="payment_methods/", null=True, blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        app_label = "core"
        db_table = "payment_methods"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
