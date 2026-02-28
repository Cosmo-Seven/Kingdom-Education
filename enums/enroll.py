from django.db import models

class EnrollStatusEnum(models.TextChoices):
    PENDING = "pending","Pending"
    APPROVED = "approved","Approved"
    CANCELLED = "cancelled","Cancelled"
    EXPIRED = "expired","Expired"