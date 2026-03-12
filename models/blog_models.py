from django.db import models
from models.base_models import BaseModel
from django.utils.text import slugify


class BlogModel(BaseModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True)
    description = models.TextField(null=True, blank=True)
    featured_image = models.ImageField(upload_to="blogs", null=True, blank=True)
    category = models.ForeignKey(
        "core.BlogCategoryModel",
        on_delete=models.CASCADE,
        related_name="blogs",
    )
    is_popular = models.BooleanField(default=False)
    link = models.URLField(null=True)
    def __str__(self):
        return self.title

    class Meta:
        app_label = "core"
        db_table = "blogs"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
