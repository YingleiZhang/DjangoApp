from django.contrib import admin
from . import models

# Register your models here.
class ItemAdmin(admin.ModelAdmin):
	list_display = ["name", "priority", "difficulty", "created", "done"]
	search_fields = ["name"]

class ItemInline(admin.TabularInline):
	model = models.Item

class DateAdmin(admin.ModelAdmin):
	list_display = ["datetime"]
	inlines = [ItemInline]
	

admin.site.register(models.Item, ItemAdmin)
admin.site.register(models.DateTime, DateAdmin)
