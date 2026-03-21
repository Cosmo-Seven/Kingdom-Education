from django.db import models
from models.base_models import BaseModel
from django.utils.text import slugify

class PartnerModel(BaseModel):
    title = models.CharField(max_length=150,null=True,blank=True)
    logo = models.ImageField(upload_to="partner/",null=True,blank=True)
    link = models.URLField(null=True)
    about = models.TextField(null=True)
    def __str__(self):
        return self.title
    
    class Meta:
        app_label = "core"
        db_table = "partner_model"
        verbose_name = "Partner"
        verbose_name_plural = "Partners"
