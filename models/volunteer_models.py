from django.db import models
from models.base_models import BaseModel


class VolunteerModel(BaseModel):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    department = models.CharField(max_length=100)
    image = models.ImageField(upload_to="volunteer")
    about = models.TextField(null=True)
    phone  = models.CharField(max_length=100,null=True)
    email = models.EmailField(max_length=150,null=True)

    class Meta:
        app_label = "core"
        db_table = "volunteer"

    def __str__(self):
        return self.name
