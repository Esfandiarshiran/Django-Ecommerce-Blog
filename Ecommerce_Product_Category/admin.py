from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import ProductsCategory


# Register your models here.

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'name']

    class Meta:
        model = ProductsCategory


admin.site.register(ProductsCategory, ProductCategoryAdmin)

