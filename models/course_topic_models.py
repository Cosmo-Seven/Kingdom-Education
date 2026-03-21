from django.db import models
from models.base_models import BaseModel
from django.utils.text import slugify


class CourseTopicModel(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    featured_image = models.ImageField(
        upload_to="course_topic_images/", null=True, blank=True
    )
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        app_label = "core"
        db_table = "course_topics"
        verbose_name = "Course Topic"
        verbose_name_plural = "Course Topics"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
