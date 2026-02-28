
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from core.models import LanguageModel, TextKeyModel, TranslationModel
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from utils.decorators import custom_login_required
from decorators.role_decorators import role_permission_required


def translation_list(request):
    languages = LanguageModel.objects.all()
    text_keys = TextKeyModel.objects.all().order_by("key")

    translations = {
        f"{t.text_key_id}|{t.language.code}": t.translated_text
        for t in TranslationModel.objects.all()
    }

    context = {
        "languages": languages,
        "text_keys": text_keys,
        "translations": translations,
    }
    return render(request, "dashboard/translations.html", context)


@csrf_exempt
def save_translation(request):
    if request.method != "POST":
        return JsonResponse({"saved": False}, status=400)

    data = json.loads(request.body)
    text_key_id = data["key"]
    lang_code = data["lang"]
    value = data["value"]

    language = LanguageModel.objects.get(code=lang_code)

    translation, _ = TranslationModel.objects.get_or_create(
        text_key_id=text_key_id,    
        language=language,
    )
    translation.translated_text = value
    translation.save()

    return JsonResponse({"saved": True})


# ========================
# Text_key Create
# ========================
@custom_login_required("dashboard_login")
@role_permission_required("add_textkeymodel")
def text_key_create(request):
    try:
        if request.method == "POST":
            key = request.POST.get("key")
            default_text = request.POST.get("default_text")

            text_key = TextKeyModel.objects.create(
                key=key,
                default_text=default_text,
            )
            text_key.save()

            messages.success(request, "Text key is created successfully")
            return redirect("translation_list")
    except Exception as e:
        messages.error(request, f"Error : {str(e)}")
        return redirect("translation_list")


# ========================
# Text_key Update
# ========================
@custom_login_required("dashboard_login")
@role_permission_required("change_textkeymodel")
def text_key_update(request, pk):
    try:
        text_key = get_object_or_404(TextKeyModel, id=pk)

        if request.method == "POST":
            key = request.POST.get("key")
            default_text = request.POST.get("default_text")

            text_key.key = key
            text_key.default_text = default_text
            text_key.save()
            messages.success(request, "Text key was updated!")
            return redirect("translation_list")
    except Exception as e:
        messages.error(request, f"Error : {str(e)}")
        return redirect("translation_list")


# ========================
# Text_key Delete
# ========================
@custom_login_required("dashboard_login")
@role_permission_required("delete_textkeymodel")
def text_key_delete(request, pk):
    try:
        text_key = get_object_or_404(TextKeyModel, id=pk)
        text_key.delete()
        messages.success(request, "Text key has been deleted!")
        return redirect("translation_list")
    except Exception as e:
        messages.error(request, f"Error : {str(e)}")
        return redirect("translation_list")
