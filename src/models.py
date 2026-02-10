from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


class Contact(models.Model):
    full_name = models.CharField(max_length=100, verbose_name="Full Name")
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name="Message")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Received At")
    is_read = models.BooleanField(default=False, verbose_name="Read")

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"

    def __str__(self):
        return f"{self.full_name} <{self.email}>"

class About(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    content = RichTextField(verbose_name="Content")

class Homepage(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    content = RichTextField(verbose_name="Content")

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    content = RichTextField(verbose_name="Content")
    link = models.URLField(max_length=500, blank=False, null=False, verbose_name="Link")

    def __str__(self):
        return self.title

class Setting(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title")
    description = models.CharField(max_length=255, verbose_name="Content")
    keywords = models.CharField(
        max_length=255, verbose_name="Keywords")
    email = models.EmailField()
    address = models.TextField(verbose_name="Address")

class Skill(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=100, verbose_name="Skill Name")

    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"
        ordering = ['name']

    def __str__(self):
        return self.name