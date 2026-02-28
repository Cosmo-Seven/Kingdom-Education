from core.models import LanguageModel


def languages(request):
    languages = LanguageModel.objects.all()
    return {"languages": languages}