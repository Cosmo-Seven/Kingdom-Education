from django.db import models
from models.base_models import BaseModel


class ProgramModel(BaseModel):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
    class Meta:
        app_label = "core"
        db_table = "program_model"
        verbose_name = "Program"
        verbose_name_plural = "Programs"