from django.contrib import admin
from .models import Post, Comment, PostsCategory


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'publish_date')
    list_filter = ('status', 'publish_date', 'create_date')
    search_fields = ('title', 'body')
    ordering = ('status', 'publish_date')
    date_hierarchy = 'publish_date'
    # prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')

@admin.register(PostsCategory)
class PostsCategoryAdmin(admin.ModelAdmin):
    list_display = ('title','slug')
    search_fields = ('title','slug')