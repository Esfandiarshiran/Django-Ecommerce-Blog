from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField
import os
from django.urls import reverse
from taggit.managers import TaggableManager  # For use taggit (the third-party app for tagging our post, products, etc.)
# using for making uniq slug
import random
from .utils import unique_slug_generator
from django.db.models.signals import pre_save
from django.db.models import Q


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"blog_posts/{final_name}"


class PostsCategory(models.Model):
    title = models.CharField(max_length=150)
    slug = models.CharField(max_length=300, unique=True, blank=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


def PostsCategory_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(PostsCategory_pre_save_receiver, sender=PostsCategory)


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class PostManager(models.Manager):
    def get_queryset(self):
        return super(PostManager, self).get_queryset().filter(status='published')

    def search(self, query):
        lookup = (
                Q(title__icontains=query)|
                Q(tags__slug__icontains=query)|
                Q(body__icontains=query)

        )
        return self.get_queryset().filter(lookup).distinct()


class Post(models.Model):
    STATUS_CHOICES = (('draft', 'Draft'), ('published', 'Published'),)
    title = models.CharField(max_length=300)
    slug = models.CharField(max_length=300, unique=True, blank=True)
    post_explanation = models.TextField(max_length=300, verbose_name="Explain about post in 300 character", default="")
    body = RichTextField(max_length=500000)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    picture = models.ImageField(upload_to=upload_image_path, null=True, blank=False, verbose_name='Picture(950*460)')
    category = models.ManyToManyField(PostsCategory, blank=False)
    tags = TaggableManager(
        verbose_name='post Tags')  # to use tagging our post just we need to add this, and migrate to DB as well.
    visit_count = models.IntegerField(default=0, verbose_name='Visiting Number')
    objects = models.Manager()
    published = PublishedManager()
    searched= PostManager()

    class Meta:
        ordering = ('-publish_date',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/blog/post/{self.slug.replace(' ', '-')}/{self.id}"


def Post_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(Post_pre_save_receiver, sender=Post)


# ________________________________________________________________________________


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    # Selecting all comments for every single post by ====> post.comments.all()
    # we can use it easily in post_detail because have post object,and instead of writing
    # post.comment_set.object.all() we could write post.comment.all()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'
