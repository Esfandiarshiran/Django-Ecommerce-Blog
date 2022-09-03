from django.contrib import admin
from .models import Product, SliderPicture, ProductGallery


# Register your models here.
#
# admin.site.register([Product, SliderPicture, ProductGallery])

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'active', 'is_free', 'hotitem', 'visit_count')
    list_filter = ('title', 'price', 'active', 'is_free', 'hotitem', 'visit_count')
    search_fields = ('title', 'price', 'active', 'is_free', 'hotitem', 'visit_count')
    ordering = ('title', 'price', 'active', 'is_free', 'hotitem', 'visit_count')


@admin.register(SliderPicture)
class SliderPictureAdmin(admin.ModelAdmin):
    list_display = ('title', 'link')
    list_filter = ('title', 'link')
    search_fields = ('title', 'link')
    ordering = ('title', 'link')


@admin.register(ProductGallery)
class ProductGalleryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    ordering = ('title',)
