from django.db import models
from models.base_models import BaseModel



class SiteModel(BaseModel):
    title = models.CharField(max_length=255)
    favicon = models.ImageField(upload_to="favicon")
    logo = models.ImageField(upload_to="logo", null=True)

    def __str__(self):
        return self.title

    class Meta:
        app_label = "core"
        db_table = "sites"
        verbose_name = "Site"
        verbose_name_plural = "Sites"