from django.db import models
from models.base_models import BaseModel
from enums.donation import StatusEnum


class DonationModel(BaseModel):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=150)
    amount = models.BigIntegerField(default=0)
    payment = models.CharField(max_length=150)
    program = models.ManyToManyField("core.ProgramModel", related_name="donations")
    status = models.CharField(
        max_length=20, choices=StatusEnum.choices, default=StatusEnum.YES
    )

    def __str__(self):
        return self.name

    class Meta:
        app_label = "core"
        db_table = "donation"
        verbose_name = "Donation"
        verbose_name_plural = "Donations"
