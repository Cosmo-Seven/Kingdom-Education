from django.db import models
from models.base_models import BaseModel
from django.utils.text import slugify


class SiteModel(BaseModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    favicon = models.ImageField(upload_to="favicon")

    def __str__(self):
        return self.title

    class Meta:
        app_label = "core"
        db_table = "sites"
        verbose_name = "Site"
        verbose_name_plural = "Sites"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
