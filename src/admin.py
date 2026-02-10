from django.contrib import admin
from .models import About, Contact, Project, Setting, Skill, Homepage
from .admin_mixins import CommonMedia


class BaseAdmin(admin.ModelAdmin):

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'created_at', 'is_read')
    list_filter = ('is_read', 'created_at')
    search_fields = ('full_name', 'email', 'message')
    readonly_fields = ('full_name', 'email', 'message', 'created_at')
    date_hierarchy = 'created_at'

    actions = ['mark_as_read']

    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
        self.message_user(request, "Selected messages marked as read.")

    mark_as_read.short_description = "Mark selected as read"


class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1
    fields = ('name',)


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [SkillInline]


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'link',)


@admin.register(Homepage)
class HomepageAdmin(admin.ModelAdmin):
    list_display = ('title', 'content',)


@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
    list_display = ('title',)
