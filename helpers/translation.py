from core.models import LanguageModel, TextKeyModel, TranslationModel

def t(key, lang_code="en"):
    try:
        lang = LanguageModel.objects.get(code=lang_code)
        text_key = TextKeyModel.objects.get(key=key)
        translation = TranslationModel.objects.get(language=lang, text_key=text_key)
        return translation.translated_text
    except:
        try:
            return TextKeyModel.objects.get(key=key).default_text
        except:
            return key


def register_key(key, default_text):
    try:
        TextKeyModel.objects.get(key=key)
    except TextKeyModel.DoesNotExist:
        TextKeyModel.objects.create(key=key, default_text=default_text)
