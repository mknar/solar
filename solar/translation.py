from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(pages)
class PagesTranslationOptions(TranslationOptions):
    fields = ('title', 'content', 'seo_title', 'seo_description', 'seo_keywords',)

@register(blog)
class BlogTranslationOptions(TranslationOptions):
    fields = ('title', 'short_desc', 'desc', 'seo_title', 'seo_description', 'seo_keywords',)

@register(service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('title', 'short_desc', 'desc', 'seo_title', 'seo_description', 'seo_keywords', 'slug')