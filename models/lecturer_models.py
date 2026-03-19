from django.db import models
from models.base_models import BaseModel
from django.utils.text import slugify


class LecturerModel(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    featured_image = models.ImageField(
        upload_to="lecturer_images/", null=True, blank=True
    )
    video_url = models.CharField(max_length=255, null=True)
    position = models.CharField(max_length=255, null=True, blank=True)
    total_students = models.PositiveIntegerField(default=0)
    about = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        app_label = "core"
        db_table = "lecturers"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def save(self, *args, **kwargs):
        if self.video_url and "drive.google.com" in self.video_url:
            self.video_url = self.video_url.replace("/view", "/preview")

        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)
