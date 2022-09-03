from django.db import models
from django.db.models.signals import pre_save, post_save

from Ecommerce_products.models import Product
from .utils import unique_slug_generator


class Tag(models.Model):
    title = models.CharField(max_length=120, verbose_name='Title')
    slug = models.SlugField(verbose_name='Slug')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Set Time')
    active = models.BooleanField(default=True, verbose_name='Active/ Deactivate')
    products = models.ManyToManyField(Product, blank=True, verbose_name='Products')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'


def tag_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(tag_pre_save_receiver, sender=Tag)
