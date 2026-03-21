from django.db import models
from models.base_models import BaseModel
from services.progress_service import calculate_course_progress
from django.utils import timezone
from datetime import timedelta
from enums.enroll import EnrollStatusEnum

class EnrollModel(BaseModel):
    student = models.ForeignKey(
        "core.UserModel", on_delete=models.CASCADE, related_name="enrollments"
    )
    course = models.ForeignKey(
        "core.CourseModel", on_delete=models.CASCADE, related_name="enrollments"
    )
    status = models.CharField(max_length=20, choices=EnrollStatusEnum.choices, default=EnrollStatusEnum.PENDING)
    progress = models.PositiveIntegerField(default=0)
    enrolled_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    
    payment_method = models.ForeignKey(
        "core.PaymentMethodModel", on_delete=models.SET_NULL, null=True, blank=True
    )
    access_expires_at = models.DateTimeField(null=True, blank=True)
    screenshot = models.ImageField(
        upload_to="enroll_screenshots/", null=True, blank=True
    )
    message = models.TextField(null=True, blank=True)

    class Meta:
        app_label = "core"
        db_table = "enrollments"
        unique_together = ("student", "course")
        verbose_name = "Enrollment"
        verbose_name_plural = "Enrollments"

    def recalculate_progress(self):
        self.progress = calculate_course_progress(self.student, self.course)

        if self.progress == 100:
            self.status = "completed"
            self.completed_at = timezone.now()

        self.save(update_fields=["progress", "status", "completed_at"])

    def set_access_expiry(self):
        if self.course.access_duration_days:
            self.access_expires_at = self.enrolled_at + timedelta(
                days=self.course.access_duration_days
            )
        else:
            self.access_expires_at = None

        self.save(update_fields=["access_expires_at"])

    def has_access(self):
        if self.access_expires_at is None:
            return True

        if timezone.now() > self.access_expires_at:
            self.status = "expired"
            self.save(update_fields=["status"])
            return False

        return True
