from django.db import models
from models.base_models import BaseModel
from django.utils.text import slugify


class ContactModel(BaseModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        app_label = "core"
        db_table = "contacts"
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
