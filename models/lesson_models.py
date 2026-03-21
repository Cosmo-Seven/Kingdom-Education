from django.db import models
from models.base_models import BaseModel
from django.utils.text import slugify


class LessonModel(BaseModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True)
    video_url = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True, blank=True)
    section = models.ForeignKey(
        "core.SectionModel",
        on_delete=models.CASCADE,
        related_name="lessons",
    )

    def __str__(self):
        return self.title

    class Meta:
        app_label = "core"
        db_table = "lessons"
        verbose_name = "Lesson"
        verbose_name_plural = "Lessons"

    def save(self, *args, **kwargs):
        if self.video_url and "drive.google.com" in self.video_url:
            self.video_url = self.video_url.replace("/view", "/preview")

        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)
