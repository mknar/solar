from modeltranslation.translator import register, TranslationOptions
from .models import pages


@register(pages)
class PagesTranslationOptions(TranslationOptions):
    fields = ('title', 'content')
