from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from utils.decorators import custom_login_required
from decorators.role_decorators import role_permission_required
from core.models import UserModel, RoleModel
from datetime import datetime


# ========================
# User List
# ========================
@custom_login_required("dashboard_login")
@role_permission_required("view_usermodel")
def user_list(request):
    try:
        if request.user.role.name == settings.HYPER:
            users = UserModel.objects.all().order_by("-created_at")
            roles = RoleModel.objects.all().order_by("-created_at")
        else:
            roles = RoleModel.objects.exclude(name=settings.HYPER).order_by(
                "-created_at"
            )
            role = RoleModel.objects.get(name=settings.HYPER)
            users = UserModel.objects.exclude(role=role).order_by("-created_at")

       

        context = {
            "users":users,
            "roles": roles,
        }
        return render(request, "dashboard/user_list.html", context)
    except Exception as e:
        messages.error(request, f"Error : {str(e)}")
        return redirect("user_list")


# ========================
# User Create
# ========================
@custom_login_required("dashboard_login")
@role_permission_required("add_usermodel")
def user_create(request):
    try:
        if request.method == "POST":
            username = request.POST.get("username")
            email = request.POST.get("email")
            profile = request.FILES.get("profile")
            phone = request.POST.get("phone")
            is_active = "is_active" in request.POST
            is_staff = "is_staff" in request.POST
            is_superuser = "is_superuser" in request.POST
            role_id = request.POST.get("role")

            if UserModel.objects.filter(email=email).exists():
                messages.error(request, "Email has already been used!")
                return redirect("user_list")

            password = request.POST.get("password")
            confirm_password = request.POST.get("confirm_password")
            if password != confirm_password:
                messages.error(request, "Password does not match! Please check again!")
                return redirect("user_list")

            user = UserModel.objects.create_user(
                username=username,
                email=email,
                profile=profile,
                password=password,
                phone=phone,
                role_id=role_id,
                is_active=is_active,
                is_staff=is_staff,
                is_superuser=is_superuser,
            )
            user.save()

            messages.success(request, f"Account was created for {username}")
            return redirect("user_list")
    except Exception as e:
        messages.error(request, f"Error : {str(e)}")
        return redirect("user_list")


# ========================
# User Update
# ========================
@custom_login_required("dashboard_login")
@role_permission_required("change_usermodel")
def user_update(request, pk):
    try:
        user = get_object_or_404(UserModel, id=pk)

        if request.method == "POST":
            confirm_password = request.POST.get("confirm_password")
            password = request.POST.get("password")
            user.username = request.POST.get("username")
            user.email = request.POST.get("email")
            user.phone = request.POST.get("phone")

            if request.FILES.get("profile"):
                if user.profile:
                    user.profile.delete(save=False)
                user.profile = request.FILES.get("profile")

            user.is_active = "is_active" in request.POST
            user.is_staff = "is_staff" in request.POST
            user.is_superuser = "is_superuser" in request.POST
            user.role_id = request.POST.get("role")

            if password != confirm_password:
                messages.error(request, "Password does not match! Please check again!")
                return redirect("user_list")

            if password:
                user.set_password(password)

            user.save()
            messages.success(request, "User was updated!")
            return redirect("user_list")

    except Exception as e:
        messages.error(request, f"Error : {str(e)}")
        return redirect("user_list")


# ========================
# User Delete
# ========================
@custom_login_required("dashboard_login")
@role_permission_required("delete_usermodel")
def user_delete(request, pk):
    try:
        user = get_object_or_404(UserModel, id=pk)

        if user.profile:
            user.profile.delete(save=False)

        user.delete()

        messages.success(request, "User has been deleted!")
        return redirect("user_list")

    except Exception as e:
        messages.error(request, f"Error : {str(e)}")
        return redirect("user_list")