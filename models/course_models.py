from django.db import models
from models.base_models import BaseModel
from django.utils.text import slugify


class CourseModel(BaseModel):
    LEVEL_CHOICES = [
        ("beginner", "Beginner"),
        ("intermediate", "Intermediate"),
        ("advanced", "Advanced"),
    ]
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    description = models.TextField()
    featured_image = models.ImageField(
        upload_to="course_images/", null=True, blank=True
    )
    topic = models.ForeignKey(
        "core.CourseTopicModel",
        on_delete=models.CASCADE,
        related_name="courses",
        null=True,
        blank=True,
    )
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default="beginner")
    enrollment_count = models.PositiveIntegerField(default=0)
    regular_price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    learning_outcomes = models.TextField(null=True, blank=True)
    requirements = models.TextField(null=True, blank=True)
    lecturers = models.ManyToManyField(
        "core.LecturerModel", related_name="courses", blank=True
    )
    access_duration_days = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text="Number of days student can access this course. Leave blank for lifetime access.",
    )
    is_popular = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        app_label = "core"
        db_table = "courses"
        verbose_name = "Course"
        verbose_name_plural = "Courses"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
