from django.db import models
from django.core.exceptions import ValidationError
from ckeditor.fields import RichTextField


class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.pk and self.__class__.objects.exists():
            raise ValidationError(f"Only one {self.__class__.__name__} instance is allowed.")
        return super().save(*args, **kwargs)


class Homepage(SingletonModel):
    title = models.CharField(max_length=200)
    content = RichTextField()

    class Meta:
        verbose_name = "Homepage"
        verbose_name_plural = "Homepage"


class About(SingletonModel):
    title = models.CharField(max_length=200)
    content = RichTextField()

    class Meta:
        verbose_name = "About"
        verbose_name_plural = "About"


class Project(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()
    link = models.URLField(max_length=500)
    
    class Meta:
        ordering = ['-title']
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.title


class Skill(models.Model):
    about = models.ForeignKey(
        About,
        on_delete=models.CASCADE,
        related_name='skills'
    )
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']
        verbose_name = "Skill"
        verbose_name_plural = "Skills"

    def __str__(self):
        return self.name


class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"

    def __str__(self):
        return f"{self.full_name} <{self.email}>"


class Setting(SingletonModel):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    keywords = models.CharField(max_length=255)
    email = models.EmailField()

    class Meta:
        verbose_name = "Site Setting"
        verbose_name_plural = "Site Setting"
