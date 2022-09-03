from django.contrib import admin
from .models import NewsModel, WishList, UserProfile

# admin.site.register([NewsModel, WishList, UserProfile])
@admin.register(NewsModel)
class NewsModelAdmin(admin.ModelAdmin):
    list_display = ('body', 'date',)
    list_filter = ('body', 'date',)
    search_fields = ('body', 'date',)
    ordering = ('body', 'date',)

@admin.register(WishList)
class WishListAdmin(admin.ModelAdmin):
    list_display = ('title', 'date',)
    list_filter = ('title', 'date',)
    search_fields = ('title', 'date',)
    ordering = ('title', 'date',)

@admin.register(UserProfile)
class WishListAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','email','mobile','update_date','sex')
    list_filter = ('first_name', 'last_name','email','mobile','update_date','sex')
    search_fields = ('first_name', 'last_name','email','mobile','update_date','sex')
    ordering = ('first_name', 'last_name','email','mobile','update_date','sex')