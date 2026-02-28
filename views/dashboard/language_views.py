from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from utils.decorators import custom_login_required

from decorators.role_decorators import role_permission_required
from core.models import LanguageModel


# ========================
# Language List
# ========================
@custom_login_required("dashboard_login")
@role_permission_required("view_languagemodel")
def language_list(request):
    try:
        languages = LanguageModel.objects.all().order_by("created_at")

        context = {
            "languages":languages,
        }
        return render(request, "dashboard/language_list.html", context)
    except Exception as e:
        messages.error(request, f"Error : {str(e)}")
        return redirect("language_list")


# ========================
# Language Create
# ========================
@custom_login_required("dashboard_login")
@role_permission_required("add_languagemodel")
def language_create(request):
    try:
        if request.method == "POST":
            name = request.POST.get("name")
            code = request.POST.get("code")
            flag = request.FILES.get("flag")

            language = LanguageModel.objects.create(
                name=name,
                code=code,
                flag=flag,
            )
            language.save()

            messages.success(request, "Language is created with QR code successfully")
            return redirect("language_list")
    except Exception as e:
        messages.error(request, f"Error : {str(e)}")
        return redirect("language_list")


# ========================
# Language Update
# ========================
@custom_login_required("dashboard_login")
@role_permission_required("change_languagemodel")
def language_update(request, pk):
    try:
        language = get_object_or_404(LanguageModel, id=pk)

        if request.method == "POST":
            name = request.POST.get("name")
            code = request.POST.get("code")
            flag = request.FILES.get("flag")

            language.name = name
            language.code = code
            if flag:
                if language.flag:
                    language.flag.delete()
                language.flag = flag
            language.save()
            messages.success(request, "Language was updated!")
            return redirect("language_list")
    except Exception as e:
        messages.error(request, f"Error : {str(e)}")
        return redirect("language_list")


# ========================
# Language Delete
# ========================
@custom_login_required("dashboard_login")
@role_permission_required("delete_languagemodel")
def language_delete(request, pk):
    try:
        language = get_object_or_404(LanguageModel, id=pk)
        if language.flag:
            language.flag.delete()
        language.delete()
        messages.success(request, "Language has been deleted!")
        return redirect("language_list")
    except Exception as e:
        messages.error(request, f"Error : {str(e)}")
        return redirect("language_list")