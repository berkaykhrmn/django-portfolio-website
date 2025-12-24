from modeltranslation.translator import register, TranslationOptions
from .models import About, Project, Setting, Homepage


@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)

@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)

@register(Setting)
class SettingTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'keywords',)

@register(Homepage)
class HomepageTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)
