from django.contrib import admin

# Register your models here.
from Ecommerce_Tag.models import Tag

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp', 'slug', 'active',)
    list_filter = ('title', 'timestamp', 'slug', 'active',)
    search_fields = ('title', 'timestamp', 'slug', 'active',)
    ordering = ('title', 'timestamp', 'slug', 'active',)
