from django.db import models
from models.base_models import BaseModel
from django.utils.text import slugify


class FileModel(BaseModel):
    file = models.FileField(upload_to="lesson_files/", null=True, blank=True)
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    description = models.TextField(null=True, blank=True)
    lesson = models.ForeignKey(
        "core.LessonModel",
        on_delete=models.CASCADE,
        related_name="files",
    )

    def __str__(self):
        return self.title

    class Meta:
        app_label = "core"
        db_table = "files"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
