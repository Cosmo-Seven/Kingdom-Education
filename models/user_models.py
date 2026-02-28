from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from managers.user_managers import UserManager
from models.base_models import BaseModel
from django.utils.timezone import now
from datetime import timedelta
from django.utils.text import slugify


class UserModel(AbstractBaseUser, PermissionsMixin, BaseModel):
    GENDER_CHOICES = [
        ("male", "Male"),
        ("female", "Female"),
        ("other", "Other"),
    ]
    username = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    email = models.EmailField(unique=True)
    role = models.ForeignKey("core.RoleModel", on_delete=models.SET_NULL, null=True)
    phone = models.CharField(max_length=50, null=True)
    profile = models.ImageField(upload_to="profile", null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    last_active = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        app_label = "core"
        db_table = "users"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.username)
        super().save(*args, **kwargs)

    def has_permission(self, perm_codename):
        if self.is_superuser:
            return True
        return (
            self.role and self.role.permissions.filter(codename=perm_codename).exists()
        )

    def has_module_perms(self, app_label):
        return (
            self.role
            and self.role.permissions.filter(content_type__app_label=app_label).exists()
        )

    def get_all_permission_ids(self):
        role_perms = set()
        if self.role:
            role_perms = set(self.role.permissions.values_list("id", flat=True))
            user_perms = set(self.user_permissions.values_list("id", flat=True))
            return role_perms.union(user_perms)

    def is_online(self):
        return self.last_active >= now() - timedelta(minutes=5)
