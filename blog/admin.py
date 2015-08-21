from django_markdown.admin import MarkdownModelAdmin
from django.contrib import admin
from . import models

# Register your models here.
class PostAdmin(MarkdownModelAdmin):
	list_display = ("title", "created")
	prepopulated_fields = {"slug": ("title",)}

admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Tag)
