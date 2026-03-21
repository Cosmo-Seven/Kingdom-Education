from django.db import models
from models.base_models import BaseModel


class LanguageModel(BaseModel):
    flag = models.ImageField(upload_to="flags/", null=True)
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        app_label = "core"
        db_table = "languages"
        verbose_name = "Language"
        verbose_name_plural = "Languages"
