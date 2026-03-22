from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from utils.decorators import custom_login_required
from helpers.allowed_models import get_allowed_models
from core.models import RoleModel
from datetime import datetime
from django.contrib.auth.models import Permission
from collections import defaultdict
from decorators.role_decorators import role_permission_required


# ========================
# Role List
# ========================
@custom_login_required("dashboard_login")
@role_permission_required("view_rolemodel")
def role_list(request):
    ALLOWED_MODELS = get_allowed_models()
    try:
        if request.user.role.name == settings.HYPER:
            roles = RoleModel.objects.all().order_by("-created_at")
        else:
            roles = RoleModel.objects.exclude(name=settings.HYPER).order_by(
                "-created_at"
            )

     

        permissions = (
            Permission.objects.filter(
                content_type__app_label="core", content_type__model__in=ALLOWED_MODELS
            )
            .exclude(codename__icontains="logentry")
            .select_related("content_type")
            .order_by("content_type__model", "codename")
        )

        modules = defaultdict(
            lambda: {"view": None, "add": None, "change": None, "delete": None}
        )

        for p in permissions:
            model_class = p.content_type.model_class()
            model_name = model_class._meta.verbose_name.title()
            codename = p.codename.lower()
            if codename.startswith("add_"):
                modules[model_name]["add"] = p
            elif codename.startswith("change_"):
                modules[model_name]["change"] = p
            elif codename.startswith("view_"):
                modules[model_name]["view"] = p
            elif codename.startswith("delete_"):
                modules[model_name]["delete"] = p

        grouped_permissions = sorted(modules.items(), key=lambda x: x[0].lower())

        context = {
            "roles": roles,
            "grouped_permissions": grouped_permissions
        }
        return render(request, "dashboard/role_list.html", context)

    except Exception as e:
        messages.error(request, f"Error: {str(e)}")
        return redirect("role_list")


# ========================
# Role Create
# ========================
@custom_login_required("dashboard_login")
@role_permission_required("add_rolemodel")
def role_create(request):
    try:
        if request.method == "POST":
            name = request.POST.get("name")

            if RoleModel.objects.filter(name=name).exists():
                messages.error(request, "Role Name already exists.")
                return redirect("role_list")

            selected_permissions = request.POST.getlist("permissions")
            if not selected_permissions:
                messages.warning(request, "Please select at least one permission.")
                return redirect("role_list")

            role = RoleModel.objects.create(name=name)
            role.permissions.set(selected_permissions)
            role.save()

            messages.success(request, "Role created successfully.")
            return redirect("role_list")

        return redirect("role_list")

    except Exception as e:
        messages.error(request, f"Error: {str(e)}")
        return redirect("role_list")


# ========================
# Role Update
# ========================
@custom_login_required("dashboard_login")
@role_permission_required("change_rolemodel")
def role_update(request, pk):
    try:
        role = get_object_or_404(RoleModel, id=pk)

        if request.method == "POST":
            name = request.POST.get("name")
            selected_permissions = set(map(int, request.POST.getlist("permissions")))
            current_permissions = set(role.permissions.values_list("id", flat=True))

            if role.name == name and selected_permissions == current_permissions:
                messages.info(request, "No changes were made.")
                return redirect("role_list")

            role.name = name
            role.permissions.set(selected_permissions)
            role.save()

            messages.success(request, "Role updated successfully.")
            return redirect("role_list")

        return redirect("role_list")

    except Exception as e:
        messages.error(request, f"Error: {str(e)}")
        return redirect("role_list")


# ========================
# Role Delete
# ========================
@custom_login_required("dashboard_login")
@role_permission_required("delete_rolemodel")
def role_delete(request, pk):
    try:
        role = get_object_or_404(RoleModel, id=pk)
        role.delete()
        messages.success(request, "Role deleted successfully.")
        return redirect("role_list")

    except Exception as e:
        messages.error(request, f"Error: {str(e)}")
        return redirect("role_list")
