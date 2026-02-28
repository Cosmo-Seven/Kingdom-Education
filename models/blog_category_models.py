from django.db import models
from models.base_models import BaseModel
from django.utils.text import slugify


class BlogCategoryModel(BaseModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True)
 

    def __str__(self):
        return self.name

    class Meta:
        app_label = "core"
        db_table = "blog_categories"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
