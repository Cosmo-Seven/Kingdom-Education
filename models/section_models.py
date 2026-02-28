from django.db import models
from models.base_models import BaseModel
from django.utils.text import slugify


class SectionModel(BaseModel):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    description = models.TextField(null=True, blank=True)
    course = models.ForeignKey(
        "core.CourseModel",
        on_delete=models.CASCADE,
        related_name="sections",
    )

    def __str__(self):
        return self.title

    class Meta:
        app_label = "core"
        db_table = "sections"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
