from django.db import models
from models.base_models import BaseModel



class HomeTextModel(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)

    def __str__(self):
        return self.title

    class Meta:
        app_label = "core"
        db_table = "Home Text"
        verbose_name = "Home Text"
        verbose_name_plural = "Home Texts"
