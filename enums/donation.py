from django.db import models

class StatusEnum(models.TextChoices):
      YES = "yes","Yes"
      NO = "no","No"


