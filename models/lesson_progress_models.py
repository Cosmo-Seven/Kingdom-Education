from django.db import models
from models.base_models import BaseModel


class LessonProgressModel(BaseModel):
    student = models.ForeignKey(
        "core.UserModel", on_delete=models.CASCADE, related_name="lesson_progresses"
    )
    lesson = models.ForeignKey(
        "core.LessonModel", on_delete=models.CASCADE, related_name="progresses"
    )
    is_completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        app_label = "core"
        unique_together = ("student", "lesson")
        db_table = "lesson_progresses"
        verbose_name = "Lesson Progress"
        verbose_name_plural = "Lesson Progresses"
