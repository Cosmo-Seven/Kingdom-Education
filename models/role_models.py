from django.db import models
from models.base_models import BaseModel
from django.utils.text import slugify


class RoleModel(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    permissions = models.ManyToManyField("auth.Permission")

    def __str__(self):
        return self.name

    class Meta:
        app_label = "core"
        db_table = "roles"
        verbose_name = "Role"
        verbose_name_plural = "Roles"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
