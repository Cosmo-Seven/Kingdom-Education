from django.shortcuts import render, redirect
from models.user_models import UserModel
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate


def login_view(request):
    if request.user.is_authenticated:
        messages.info(request, "You are already logged in.")
        return redirect("home")
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful.")
            return redirect("home")
        else:
            messages.error(request, "Invalid email or password.")
            return redirect("login")
    return render(request, "website/login.html")


def register_view(request):
    if request.user.is_authenticated:
        messages.info(request, "You are already registered and logged in.")
        return redirect("home")
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        phone = request.POST.get("phone")
        confirm_password = request.POST.get("confirm_password")
        gender = request.POST.get("gender")
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect("register")
        if UserModel.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect("register")
        user = UserModel.objects.create_user(
            username=username, email=email, password=password, gender=gender, phone=phone
        )
        login(request, user)
        messages.success(request, "Registration successful.")
        return redirect("home")
    context = {
        "gender_choices": UserModel.GENDER_CHOICES,
    }
    return render(request, "website/register.html", context)


def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("home")
